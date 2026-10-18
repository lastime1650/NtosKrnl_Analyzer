# ViPendingWorkerThread

- RVA: `0x00BA20D0`–`0x00BA2107` (길이 `55` bytes)
- VA: `0x0000000140BA20D0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF360`
- 디코드: `15`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA20EF` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00BA20FB` → [ViPendingCompleteAfterWait](ViPendingCompleteAfterWait_function_00BA1D18.md) (function, `0x00BA1D18`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA20EF` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA20D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BA20D5  57                              push rdi
00BA20D6  48 83 EC 30                     sub rsp, 0x30
00BA20DA  48 8B D9                        mov rbx, rcx
00BA20DD  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BA20E3  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00BA20E7  45 33 C9                        xor r9d, r9d
00BA20EA  45 33 C0                        xor r8d, r8d
00BA20ED  33 D2                           xor edx, edx
00BA20EF  E8 BC C5 66 FF                  call 0x14020e6b0
00BA20F4  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00BA20F8  FF 43 28                        inc dword ptr [rbx + 0x28]
00BA20FB  E8 18 FC FF FF                  call 0x140ba1d18
00BA2100  48 83 63 08 00                  and qword ptr [rbx + 8], 0
00BA2105  EB D6                           jmp 0x140ba20dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViPendingWorkerThread(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
loc_00BA20DD:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(a1 + 16, a2, a3, a4);
    result = ViPendingCompleteAfterWait(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    goto loc_00BA20DD;
}
```

## 5. (Beta) C Style

```c
int64_t ViPendingWorkerThread(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
loc_00BA20DD:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(Arg1 + 16, Arg2, Arg3, Arg4);
    result = ViPendingCompleteAfterWait(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, Arg4);
    goto loc_00BA20DD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA20D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA20D0[BB_00BA20D0]
  bb_00BA20DD[BB_00BA20DD]
  bb_00BA20D0 -->|flow| bb_00BA20DD
  bb_00BA20DD -->|branch| bb_00BA20DD
```
