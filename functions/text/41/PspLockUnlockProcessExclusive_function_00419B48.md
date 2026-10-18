# PspLockUnlockProcessExclusive

- RVA: `0x00419B48`–`0x00419B80` (길이 `56` bytes)
- VA: `0x0000000140419B48`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00419B6C` → [ExfAcquireReleasePushLockExclusive](ExfAcquireReleasePushLockExclusive_function_00419C2C.md) (function, `0x00419C2C`)
- `0x00419B74` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)

### Direct callers
- [PspSetProcessAffinityUpdateMode](../../page/78/PspSetProcessAffinityUpdateMode_function_007828D8.md) at `0x0078296A`
- [PspAssignPrimaryToken](../../page/78/PspAssignPrimaryToken_function_00784870.md) at `0x007849E0`
- [PspDisablePrimaryTokenExchange](../../page/8D/PspDisablePrimaryTokenExchange_function_008D5C10.md) at `0x008D5C41`
- [NtGetNextProcess](../../page/91/NtGetNextProcess_function_0091DF50.md) at `0x0091E206`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6114`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00419B48  40 53                           push rbx
00419B4A  48 83 EC 20                     sub rsp, 0x20
00419B4E  66 FF 8A E4 01 00 00            dec word ptr [rdx + 0x1e4]
00419B55  48 8B DA                        mov rbx, rdx
00419B58  48 81 C1 C8 01 00 00            add rcx, 0x1c8
00419B5F  90                              nop
00419B60  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00419B65  48 8B 01                        mov rax, qword ptr [rcx]
00419B68  A8 01                           test al, 1
00419B6A  74 05                           je 0x140419b71
00419B6C  E8 BB 00 00 00                  call 0x140419c2c
00419B71  48 8B CB                        mov rcx, rbx
00419B74  E8 97 54 E4 FF                  call 0x14025f010
00419B79  48 83 C4 20                     add rsp, 0x20
00419B7D  5B                              pop rbx
00419B7E  C3                              ret
00419B7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockUnlockProcessExclusive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (456);
    result = *(unsigned __int64 *)(a1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) != 0) {
        result = ExfAcquireReleasePushLockExclusive(a1, a2, a3, a4);
    }
    result = KiLeaveCriticalRegionUnsafe(a2, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLockUnlockProcessExclusive(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (456);
    result = *(uint64_t *)(arg1);
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) != 0) {
        result = ExfAcquireReleasePushLockExclusive(Arg1, Arg2, a3, a4);
    }
    result = KiLeaveCriticalRegionUnsafe(Arg2, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x1E4` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00419B48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00419B48[BB_00419B48]
  bb_00419B6C[BB_00419B6C]
  bb_00419B71[BB_00419B71]
  bb_00419B7F[BB_00419B7F]
  bb_00419B48 -->|branch| bb_00419B71
  bb_00419B48 -->|fallthrough| bb_00419B6C
  bb_00419B6C -->|flow| bb_00419B71
```
