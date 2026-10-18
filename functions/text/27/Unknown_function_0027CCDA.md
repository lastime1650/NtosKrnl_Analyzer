# sub_0027CCDA

- RVA: `0x0027CCDA`–`0x0027CD07` (길이 `45` bytes)
- VA: `0x000000014027CCDA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000661D4`
- 디코드: `14`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0027CD00` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0027CCE7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0027CCDA  44 0F 20 C3                     mov rbx, cr8
0027CCDE  B9 02 00 00 00                  mov ecx, 2
0027CCE3  44 0F 22 C1                     mov cr8, rcx
0027CCE7  83 3D 32 A0 D4 00 00            cmp dword ptr [rip + 0xd4a032], 0
0027CCEE  75 0A                           jne 0x14027ccfa
0027CCF0  0F B6 C3                        movzx eax, bl
0027CCF3  48 83 C4 20                     add rsp, 0x20
0027CCF7  5B                              pop rbx
0027CCF8  C3                              ret
0027CCF9  CC                              int3
0027CCFA  0F B6 D1                        movzx edx, cl
0027CCFD  0F B6 CB                        movzx ecx, bl
0027CD00  E8 F7 89 27 00                  call 0x1404f56fc
0027CD05  EB E9                           jmp 0x14027ccf0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0027CCDA(void)
{
    __int64 result;
    __int64 v_rsp;

    if ((*(unsigned int *)(v_rip + 13934642)) != 0) goto loc_0027CCFA;
loc_0027CCF0:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_0027CCFA:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, a3, a4);
    goto loc_0027CCF0;
}
```

## 5. (Beta) C Style

```c
void sub_0027CCDA(void)
{
    int64_t result;
    int64_t local_rsp;

    if ((*(uint32_t *)(v_rip + 0xD4A032)) != 0) goto loc_0027CCFA;
loc_0027CCF0:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_0027CCFA:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, a3, a4);
    goto loc_0027CCF0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027CCDA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0027CCDA[BB_0027CCDA]
  bb_0027CCF0[BB_0027CCF0]
  bb_0027CCF9[BB_0027CCF9]
  bb_0027CCFA[BB_0027CCFA]
  bb_0027CCDA -->|branch| bb_0027CCFA
  bb_0027CCDA -->|fallthrough| bb_0027CCF0
  bb_0027CCF9 -->|flow| bb_0027CCFA
  bb_0027CCFA -->|branch| bb_0027CCF0
```
