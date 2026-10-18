# PspAssociateCompletionPortCallback

- RVA: `0x00A83290`–`0x00A832D6` (길이 `70` bytes)
- VA: `0x0000000140A83290`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A832B2` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00A832C8` → [PspSendJobNotification](../../text/49/PspSendJobNotification_function_0049EC28.md) (function, `0x0049EC28`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A832B2` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00A832C8` → [PspSendJobNotification](../../text/49/PspSendJobNotification_function_0049EC28.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A83290  40 53                           push rbx
00A83292  48 83 EC 20                     sub rsp, 0x20
00A83296  4C 8B D9                        mov r11, rcx
00A83299  48 8B DA                        mov rbx, rdx
00A8329C  48 81 C1 F0 01 00 00            add rcx, 0x1f0
00A832A3  8B 01                           mov eax, dword ptr [rcx]
00A832A5  A8 01                           test al, 1
00A832A7  75 24                           jne 0x140a832cd
00A832A9  BA 04 00 00 00                  mov edx, 4
00A832AE  44 8D 42 1C                     lea r8d, [rdx + 0x1c]
00A832B2  E8 C1 40 A1 FF                  call 0x140497378
00A832B7  4D 8B 83 D0 01 00 00            mov r8, qword ptr [r11 + 0x1d0]
00A832BE  45 33 C9                        xor r9d, r9d
00A832C1  48 8B CB                        mov rcx, rbx
00A832C4  41 8D 51 06                     lea edx, [r9 + 6]
00A832C8  E8 5B B9 A1 FF                  call 0x14049ec28
00A832CD  33 C0                           xor eax, eax
00A832CF  48 83 C4 20                     add rsp, 0x20
00A832D3  5B                              pop rbx
00A832D4  C3                              ret
00A832D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAssociateCompletionPortCallback(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (496);
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) == 0) {
        a2 = 4;
        a3 = a2 + 28;
        result = RtlInterlockedSetClearBits(a1, a2, a3, a4);
        a3 = *(unsigned __int64 *)(a1 + 464);
        a4 = 0;
        a1 = a2;
        a2 = a4 + 6;
        result = PspSendJobNotification(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspAssociateCompletionPortCallback(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (496);
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) == 0) {
        Arg2 = 4;
        Arg3 = Arg2 + 28;
        result = RtlInterlockedSetClearBits(Arg1, Arg2, Arg3, Arg4);
        Arg3 = *(uint64_t *)(arg1 + 0x1D0);
        Arg4 = 0;
        Arg1 = Arg2;
        Arg2 = Arg4 + 6;
        result = PspSendJobNotification(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A83290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A83290[BB_00A83290]
  bb_00A832A9[BB_00A832A9]
  bb_00A832CD[BB_00A832CD]
  bb_00A832D5[BB_00A832D5]
  bb_00A83290 -->|branch| bb_00A832CD
  bb_00A83290 -->|fallthrough| bb_00A832A9
  bb_00A832A9 -->|flow| bb_00A832CD
```
