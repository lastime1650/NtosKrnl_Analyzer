# TtmpOpenQueueHandle

- RVA: `0x0077E070`–`0x0077E0B8` (길이 `72` bytes)
- VA: `0x000000014077E070`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0077E094` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x0077E0A5` → [TtmiLogQueueHandleOpened](TtmiLogQueueHandleOpened_function_0077ACF4.md) (function, `0x0077ACF4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0077E084` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0077E094` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077E070  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0077E075  57                              push rdi
0077E076  48 83 EC 20                     sub rsp, 0x20
0077E07A  45 33 D2                        xor r10d, r10d
0077E07D  49 8B D9                        mov rbx, r9
0077E080  84 D2                           test dl, dl
0077E082  8B F9                           mov edi, ecx
0077E084  4C 0F 44 05 24 8A 84 00         cmove r8, qword ptr [rip + 0x848a24]
0077E08C  4D 85 C0                        test r8, r8
0077E08F  74 0B                           je 0x14077e09c
0077E091  49 8B C8                        mov rcx, r8
0077E094  E8 77 F8 CB FF                  call 0x14043d910
0077E099  4C 8B D0                        mov r10, rax
0077E09C  44 8B C7                        mov r8d, edi
0077E09F  49 8B D2                        mov rdx, r10
0077E0A2  48 8B CB                        mov rcx, rbx
0077E0A5  E8 4A CC FF FF                  call 0x14077acf4
0077E0AA  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0077E0AF  33 C0                           xor eax, eax
0077E0B1  48 83 C4 20                     add rsp, 0x20
0077E0B5  5F                              pop rdi
0077E0B6  C3                              ret
0077E0B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpOpenQueueHandle(int a1, unsigned __int8 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_r10 = 0;
    if (a2 == 0) { a3 = *(unsigned __int64 *)(v_rip + 8686116); }
    if (a3 != 0) {
        a1 = a3;
        result = PsGetProcessId(a1, a2, a3, a4);
        v_r10 = result;
    }
    result = TtmiLogQueueHandleOpened(a4, v_r10, (unsigned int)((unsigned int)((unsigned int)(a1))), a4);
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpOpenQueueHandle(int32_t Arg1, uint8_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_r10 = 0;
    if (Arg2 == 0) { Arg3 = *(uint64_t *)(v_rip + 0x848A24); }
    if (Arg3 != 0) {
        Arg1 = Arg3;
        result = PsGetProcessId(Arg1, Arg2, Arg3, Arg4);
        local_r10 = result;
    }
    result = TtmiLogQueueHandleOpened(Arg4, local_r10, (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg4);
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077E070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077E070[BB_0077E070]
  bb_0077E091[BB_0077E091]
  bb_0077E09C[BB_0077E09C]
  bb_0077E0B7[BB_0077E0B7]
  bb_0077E070 -->|branch| bb_0077E09C
  bb_0077E070 -->|fallthrough| bb_0077E091
  bb_0077E091 -->|flow| bb_0077E09C
```
