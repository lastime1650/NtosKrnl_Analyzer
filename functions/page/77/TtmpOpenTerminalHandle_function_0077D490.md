# TtmpOpenTerminalHandle

- RVA: `0x0077D490`–`0x0077D4DE` (길이 `78` bytes)
- VA: `0x000000014077D490`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0077D4B7` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (function, `0x0043D910`)
- `0x0077D4CB` → [TtmiLogTerminalHandleOpened](TtmiLogTerminalHandleOpened_function_0077BF4C.md) (function, `0x0077BF4C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0077D4A7` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0077D4B7` → [PsGetProcessId](../../text/43/PsGetProcessId_function_0043D910.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077D490  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0077D495  57                              push rdi
0077D496  48 83 EC 20                     sub rsp, 0x20
0077D49A  4D 8B D0                        mov r10, r8
0077D49D  49 8B D9                        mov rbx, r9
0077D4A0  45 33 C0                        xor r8d, r8d
0077D4A3  8B F9                           mov edi, ecx
0077D4A5  84 D2                           test dl, dl
0077D4A7  4C 0F 44 15 01 96 84 00         cmove r10, qword ptr [rip + 0x849601]
0077D4AF  4D 85 D2                        test r10, r10
0077D4B2  74 0B                           je 0x14077d4bf
0077D4B4  49 8B CA                        mov rcx, r10
0077D4B7  E8 54 04 CC FF                  call 0x14043d910
0077D4BC  4C 8B C0                        mov r8, rax
0077D4BF  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0077D4C3  44 8B CF                        mov r9d, edi
0077D4C6  8B 53 1C                        mov edx, dword ptr [rbx + 0x1c]
0077D4C9  8B 09                           mov ecx, dword ptr [rcx]
0077D4CB  E8 7C EA FF FF                  call 0x14077bf4c
0077D4D0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0077D4D5  33 C0                           xor eax, eax
0077D4D7  48 83 C4 20                     add rsp, 0x20
0077D4DB  5F                              pop rdi
0077D4DC  C3                              ret
0077D4DD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpOpenTerminalHandle(int a1, unsigned __int8 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    if (a2 == 0) { a3 = *(unsigned __int64 *)(v_rip + 8689153); }
    if (a3 != 0) {
        a1 = a3;
        result = PsGetProcessId(a1, a2, a3, a4);
        a3 = result;
    }
    result = TtmiLogTerminalHandleOpened((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))), (unsigned int)(*(unsigned int *)(a4 + 28)), a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpOpenTerminalHandle(int32_t Arg1, uint8_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    if (Arg2 == 0) { Arg3 = *(uint64_t *)(v_rip + 0x849601); }
    if (Arg3 != 0) {
        Arg1 = Arg3;
        result = PsGetProcessId(Arg1, Arg2, Arg3, Arg4);
        Arg3 = result;
    }
    result = TtmiLogTerminalHandleOpened((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x10))), (uint32_t)(*(uint32_t *)(arg4 + 0x1C)), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077D490&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077D490[BB_0077D490]
  bb_0077D4B4[BB_0077D4B4]
  bb_0077D4BF[BB_0077D4BF]
  bb_0077D4DD[BB_0077D4DD]
  bb_0077D490 -->|branch| bb_0077D4BF
  bb_0077D490 -->|fallthrough| bb_0077D4B4
  bb_0077D4B4 -->|flow| bb_0077D4BF
```
