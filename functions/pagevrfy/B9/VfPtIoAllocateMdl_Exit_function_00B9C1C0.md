# VfPtIoAllocateMdl_Exit

- RVA: `0x00B9C1C0`–`0x00B9C1FF` (길이 `63` bytes)
- VA: `0x0000000140B9C1C0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9C1C9` → [VfIsKernelVerificationOn](../../text/4F/VfIsKernelVerificationOn_function_004FCC90.md) (function, `0x004FCC90`)
- `0x00B9C1F3` → [VfPtMiscPoolNotification](../../text/3F/VfPtMiscPoolNotification_function_003FF310.md) (function, `0x003FF310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9C1DB` → RVA `0x00E681A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B9C1C9` → [VfIsKernelVerificationOn](../../text/4F/VfIsKernelVerificationOn_function_004FCC90.md) (`PAGEVRFY` → `.text`)
  - `0x00B9C1F3` → [VfPtMiscPoolNotification](../../text/3F/VfPtMiscPoolNotification_function_003FF310.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9C1C0  40 53                           push rbx
00B9C1C2  48 83 EC 20                     sub rsp, 0x20
00B9C1C6  48 8B D9                        mov rbx, rcx
00B9C1C9  E8 C2 0A 96 FF                  call 0x1404fcc90
00B9C1CE  84 C0                           test al, al
00B9C1D0  75 26                           jne 0x140b9c1f8
00B9C1D2  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00B9C1D6  48 85 C9                        test rcx, rcx
00B9C1D9  74 1D                           je 0x140b9c1f8
00B9C1DB  8B 05 BF BF 2C 00               mov eax, dword ptr [rip + 0x2cbfbf]
00B9C1E1  A8 01                           test al, 1
00B9C1E3  75 13                           jne 0x140b9c1f8
00B9C1E5  48 0F BF 51 08                  movsx rdx, word ptr [rcx + 8]
00B9C1EA  45 33 C9                        xor r9d, r9d
00B9C1ED  41 B8 4D 64 6C 20               mov r8d, 0x206c644d
00B9C1F3  E8 18 31 86 FF                  call 0x1403ff310
00B9C1F8  48 83 C4 20                     add rsp, 0x20
00B9C1FC  5B                              pop rbx
00B9C1FD  C3                              ret
00B9C1FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfPtIoAllocateMdl_Exit(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VfIsKernelVerificationOn(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B9C1F8;
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_00B9C1F8;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2932671));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2932671)))) & (1)) == 0) {
        a2 = (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + 8));
        a4 = 0;
        a3 = 0x206C644DULL;
        result = VfPtMiscPoolNotification(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfPtIoAllocateMdl_Exit(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VfIsKernelVerificationOn(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B9C1F8;
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_00B9C1F8;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x2CBFBF));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2CBFBF)))) & (1)) == 0) {
        Arg2 = (int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8));
        Arg4 = 0;
        Arg3 = 0x206C644DULL;
        result = VfPtMiscPoolNotification(*(uint64_t *)(arg1 + 0x28), Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9C1C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9C1C0[BB_00B9C1C0]
  bb_00B9C1D2[BB_00B9C1D2]
  bb_00B9C1DB[BB_00B9C1DB]
  bb_00B9C1E5[BB_00B9C1E5]
  bb_00B9C1F8[BB_00B9C1F8]
  bb_00B9C1FE[BB_00B9C1FE]
  bb_00B9C1C0 -->|branch| bb_00B9C1F8
  bb_00B9C1C0 -->|fallthrough| bb_00B9C1D2
  bb_00B9C1D2 -->|branch| bb_00B9C1F8
  bb_00B9C1D2 -->|fallthrough| bb_00B9C1DB
  bb_00B9C1DB -->|branch| bb_00B9C1F8
  bb_00B9C1DB -->|fallthrough| bb_00B9C1E5
  bb_00B9C1E5 -->|flow| bb_00B9C1F8
```
