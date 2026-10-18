# sub_002875EF

- RVA: `0x002875EF`–`0x00287607` (길이 `24` bytes)
- VA: `0x00000001402875EF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066CEC`
- 디코드: `5`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002875FF` → [sub_00287DEA](Unknown_function_00287DEA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002875EF  4C 89 AC 24 08 01 00 00         mov qword ptr [rsp + 0x108], r13
002875F7  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
002875FC  66 85 C0                        test ax, ax
002875FF  0F 85 E5 07 00 00               jne 0x140287dea
00287605  33 D2                           xor edx, edx
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002875EF(__int64 a1, int a2)
{
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p38;

    v_stack_p108 = v_r13;
    v_stack_p38 = (unsigned int)(v_r12);
    a2 = 0;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_002875EF(int64_t Arg1, int32_t Arg2)
{
    uint64_t v_stack_p108;
    uint32_t v_stack_p38;

    v_stack_p108 = local_r13;
    v_stack_p38 = (uint32_t)(local_r12);
    Arg2 = 0;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002875EF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002875EF[BB_002875EF]
  bb_00287605[BB_00287605]
  bb_002875EF -->|fallthrough| bb_00287605
```
