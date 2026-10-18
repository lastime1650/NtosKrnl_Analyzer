# sub_00358636

- RVA: `0x00358636`–`0x00358656` (길이 `32` bytes)
- VA: `0x0000000140358636`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079768`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0035863E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00358636  44 0F 20 C1                     mov rcx, cr8
0035863A  40 0F B6 D7                     movzx edx, dil
0035863E  E8 55 D0 19 00                  call 0x1404f5698
00358643  40 0F B6 CF                     movzx ecx, dil
00358647  44 0F 22 C1                     mov cr8, rcx
0035864B  0F B6 C3                        movzx eax, bl
0035864E  48 83 C4 78                     add rsp, 0x78
00358652  5F                              pop rdi
00358653  5B                              pop rbx
00358654  C3                              ret
00358655  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00358636(void)
{
    __int64 result;
    __int64 v_rsp;

    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (unsigned __int8)(v_rdi), a3, a4);
    v_rsp = (v_rsp) + (120);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void sub_00358636(void)
{
    int64_t result;
    int64_t local_rsp;

    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (uint8_t)(local_rdi), a3, a4);
    local_rsp = (local_rsp) + (120);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00358636&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00358636[BB_00358636]
  bb_00358655[BB_00358655]
```
