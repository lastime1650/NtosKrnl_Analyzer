# PopResetIdlePhaseWatchdogDiagnosticContext

- RVA: `0x009149B4`–`0x009149FD` (길이 `73` bytes)
- VA: `0x00000001409149B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A618`
- 디코드: `16`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009149BF` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x009149DE` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x009149EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopDisarmIdlePhaseWatchdog](PopDisarmIdlePhaseWatchdog_function_00914408.md) at `0x00914454`

### Static image references
- `0x009149B8` → RVA `0x00F08488` (`.data`; read)
- `0x009149C4` → RVA `0x00F08498` (`.data`; read)
- `0x009149CB` → RVA `0x00F084A0` (`.data`; read/write)
- `0x009149F3` → RVA `0x00F08498` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009149BF` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x009149DE` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x009149EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009149B4  48 83 EC 28                     sub rsp, 0x28
009149B8  48 8D 0D C9 3A 5F 00            lea rcx, [rip + 0x5f3ac9]
009149BF  E8 80 C1 B1 FF                  call 0x140430b44
009149C4  48 8B 0D CD 3A 5F 00            mov rcx, qword ptr [rip + 0x5f3acd]
009149CB  83 25 CE 3A 5F 00 00            and dword ptr [rip + 0x5f3ace], 0
009149D2  48 85 C9                        test rcx, rcx
009149D5  75 12                           jne 0x1409149e9
009149D7  48 8D 0D AA 3A 5F 00            lea rcx, [rip + 0x5f3aaa]
009149DE  E8 D9 B1 9C FF                  call 0x1402dfbbc
009149E3  48 83 C4 28                     add rsp, 0x28
009149E7  C3                              ret
009149E8  CC                              int3
009149E9  BA 50 64 69 67                  mov edx, 0x67696450
009149EE  E8 7D DE 26 00                  call 0x140b82870
009149F3  48 83 25 9D 3A 5F 00 00         and qword ptr [rip + 0x5f3a9d], 0
009149FB  EB DA                           jmp 0x1409149d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopResetIdlePhaseWatchdogDiagnosticContext(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 6240969, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rip + 6240973) != 0) goto loc_009149E9;
loc_009149D7:
    result = PopReleaseRwLock(v_rip + 6240938, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_009149E9:
    result = ExFreePoolWithTag(v_rip + 6240938, (unsigned int)(0x67696450ULL), a3, a4);
    goto loc_009149D7;
}
```

## 5. (Beta) C Style

```c
void PopResetIdlePhaseWatchdogDiagnosticContext(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 6240969, a2, a3, a4);
    if (*(uint64_t *)(v_rip + 0x5F3ACD) != 0) goto loc_009149E9;
loc_009149D7:
    result = PopReleaseRwLock(v_rip + 6240938, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_009149E9:
    result = ExFreePoolWithTag(v_rip + 6240938, (uint32_t)(0x67696450ULL), a3, a4);
    goto loc_009149D7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009149B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009149B4[BB_009149B4]
  bb_009149D7[BB_009149D7]
  bb_009149E8[BB_009149E8]
  bb_009149E9[BB_009149E9]
  bb_009149B4 -->|branch| bb_009149E9
  bb_009149B4 -->|fallthrough| bb_009149D7
  bb_009149E8 -->|flow| bb_009149E9
  bb_009149E9 -->|branch| bb_009149D7
```
