# CmSiRWLockReleaseExclusive

- RVA: `0x00A0DAB0`–`0x00A0DADC` (길이 `44` bytes)
- VA: `0x0000000140A0DAB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A0DAC8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A0DAD0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [CmSiAcquireProcessLockedPagesCharge](../../text/47/CmSiAcquireProcessLockedPagesCharge_function_0047D714.md) at `0x0047D7A5`
- [CmSiReleaseProcessLockedPagesCharge](../../text/47/CmSiReleaseProcessLockedPagesCharge_function_0047D81C.md) at `0x0047D89F`
- [CmSiSetProcessWorkingSetMaximum](../../text/66/CmSiSetProcessWorkingSetMaximum_function_0066DD6C.md) at `0x0066DDF6`
- [CmpVolumeManagerGetContextForFile](../95/CmpVolumeManagerGetContextForFile_function_009525A8.md) at `0x0095269F`
- [CmpVolumeContextDecrementRefCount](../9B/CmpVolumeContextDecrementRefCount_function_009B2E14.md) at `0x009B2E93`
- [CmpVolumeContextDecrementRefCount](../9B/CmpVolumeContextDecrementRefCount_function_009B2E14.md) at `0x009B2EAC`
- [CmpDumpKeyToBuffer](../../pagecmrc/BC/CmpDumpKeyToBuffer_function_00BC9130.md) at `0x00BC91BB`
- [CmpDumpKeyToBuffer](../../pagecmrc/BC/CmpDumpKeyToBuffer_function_00BC9130.md) at `0x00BC924B`
- [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) at `0x00BC9C3C`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5DEC1`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5E1DC`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5E1E8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A0DAC8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A0DAD0` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0DAB0  40 53                           push rbx
00A0DAB2  48 83 EC 20                     sub rsp, 0x20
00A0DAB6  48 8B D9                        mov rbx, rcx
00A0DAB9  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A0DABD  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
00A0DAC2  24 06                           and al, 6
00A0DAC4  3C 02                           cmp al, 2
00A0DAC6  75 05                           jne 0x140a0dacd
00A0DAC8  E8 03 83 85 FF                  call 0x140265dd0
00A0DACD  48 8B CB                        mov rcx, rbx
00A0DAD0  E8 2B 3B 8D FF                  call 0x1402e1600
00A0DAD5  48 83 C4 20                     add rsp, 0x20
00A0DAD9  5B                              pop rbx
00A0DADA  C3                              ret
00A0DADB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSiRWLockReleaseExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSiRWLockReleaseExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0DAB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A0DAB0[BB_00A0DAB0]
  bb_00A0DAC8[BB_00A0DAC8]
  bb_00A0DACD[BB_00A0DACD]
  bb_00A0DADB[BB_00A0DADB]
  bb_00A0DAB0 -->|branch| bb_00A0DACD
  bb_00A0DAB0 -->|fallthrough| bb_00A0DAC8
  bb_00A0DAC8 -->|flow| bb_00A0DACD
```
