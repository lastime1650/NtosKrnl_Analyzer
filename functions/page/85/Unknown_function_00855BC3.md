# sub_00855BC3

- RVA: `0x00855BC3`–`0x00855BD8` (길이 `21` bytes)
- VA: `0x0000000140855BC3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A19C`
- 디코드: `8`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00855BC6` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00855BC6` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00855BC3  49 8B CC                        mov rcx, r12
00855BC6  E8 B5 01 C2 FF                  call 0x140475d80
00855BCB  41 8B C7                        mov eax, r15d
00855BCE  48 83 C4 68                     add rsp, 0x68
00855BD2  41 5F                           pop r15
00855BD4  41 5C                           pop r12
00855BD6  C3                              ret
00855BD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00855BC3(void)
{
    __int64 result;
    __int64 v_rsp;

    result = CmSiFreeMemory(v_r12, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)(v_r15));
}
```

## 5. (Beta) C Style

```c
void sub_00855BC3(void)
{
    int64_t result;
    int64_t local_rsp;

    result = CmSiFreeMemory(local_r12, a2, a3, a4);
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)(local_r15));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00855BC3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00855BC3[BB_00855BC3]
  bb_00855BD7[BB_00855BD7]
```
