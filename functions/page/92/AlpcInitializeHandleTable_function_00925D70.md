# AlpcInitializeHandleTable

- RVA: `0x00925D70`–`0x00925DBE` (길이 `78` bytes)
- VA: `0x0000000140925D70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `22`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00925D89` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (function, `0x003FB730`)
- `0x00925DA9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [AlpcpCreateClientPort](AlpcpCreateClientPort_function_009270AC.md) at `0x0092738B`
- [AlpcpCreateConnectionPort](../9E/AlpcpCreateConnectionPort_function_009E70B0.md) at `0x009E722F`

### Static image references
- `0x00925D82` → RVA `0x00E27280` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00925D89` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (`PAGE` → `.text`)
  - `0x00925DA9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00925D70  40 53                           push rbx
00925D72  48 83 EC 20                     sub rsp, 0x20
00925D76  83 61 18 00                     and dword ptr [rcx + 0x18], 0
00925D7A  48 8B D9                        mov rbx, rcx
00925D7D  48 83 61 08 00                  and qword ptr [rcx + 8], 0
00925D82  48 8D 0D F7 14 50 00            lea rcx, [rip + 0x5014f7]
00925D89  E8 A2 59 AD FF                  call 0x1403fb730
00925D8E  48 89 03                        mov qword ptr [rbx], rax
00925D91  48 85 C0                        test rax, rax
00925D94  74 21                           je 0x140925db7
00925D96  33 D2                           xor edx, edx
00925D98  48 C7 43 10 10 00 00 00         mov qword ptr [rbx + 0x10], 0x10
00925DA0  41 B8 80 00 00 00               mov r8d, 0x80
00925DA6  48 8B C8                        mov rcx, rax
00925DA9  E8 92 0E DA FF                  call 0x1406c6c40
00925DAE  33 C0                           xor eax, eax
00925DB0  48 83 C4 20                     add rsp, 0x20
00925DB4  5B                              pop rbx
00925DB5  C3                              ret
00925DB6  CC                              int3
00925DB7  B8 9A 00 00 C0                  mov eax, 0xc000009a
00925DBC  EB F2                           jmp 0x140925db0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcInitializeHandleTable(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAllocateFromPagedLookasideList(v_rip + 5248247, a2, a3, a4);
    *(unsigned __int64 *)(a1) = result;
    if (result == 0) goto loc_00925DB7;
    a2 = 0;
    *(unsigned __int64 *)(a1 + 16) = 16;
    result = memset(result, a2, 128, a4);
    result = 0;
loc_00925DB0:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00925DB7:
    goto loc_00925DB0;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcInitializeHandleTable(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAllocateFromPagedLookasideList(v_rip + 5248247, Arg2, a3, a4);
    *(uint64_t *)(arg1) = result;
    if (result == 0) goto loc_00925DB7;
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x10) = 16;
    result = memset(result, Arg2, 128, a4);
    result = 0;
loc_00925DB0:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00925DB7:
    goto loc_00925DB0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00925D70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00925D70[BB_00925D70]
  bb_00925D96[BB_00925D96]
  bb_00925DB0[BB_00925DB0]
  bb_00925DB6[BB_00925DB6]
  bb_00925DB7[BB_00925DB7]
  bb_00925D70 -->|branch| bb_00925DB7
  bb_00925D70 -->|fallthrough| bb_00925D96
  bb_00925D96 -->|flow| bb_00925DB0
  bb_00925DB6 -->|flow| bb_00925DB7
  bb_00925DB7 -->|branch| bb_00925DB0
```
