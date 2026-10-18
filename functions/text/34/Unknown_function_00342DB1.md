# sub_00342DB1

- RVA: `0x00342DB1`–`0x00342DC8` (길이 `23` bytes)
- VA: `0x0000000140342DB1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077A04`
- 디코드: `8`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00342DB8` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00342DB1  44 0F 20 C1                     mov rcx, cr8
00342DB5  0F B6 D3                        movzx edx, bl
00342DB8  E8 DB 28 1B 00                  call 0x1404f5698
00342DBD  44 0F 22 C3                     mov cr8, rbx
00342DC1  48 83 C4 20                     add rsp, 0x20
00342DC5  5B                              pop rbx
00342DC6  C3                              ret
00342DC7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00342DB1(void)
{
    __int64 result;
    __int64 v_rsp;

    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (unsigned __int8)(v_rbx), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_00342DB1(void)
{
    int64_t result;
    int64_t local_rsp;

    result = KiLowerIrqlProcessIrqlFlags(v_cr8, (uint8_t)(local_rbx), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00342DB1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00342DB1[BB_00342DB1]
  bb_00342DC7[BB_00342DC7]
```
