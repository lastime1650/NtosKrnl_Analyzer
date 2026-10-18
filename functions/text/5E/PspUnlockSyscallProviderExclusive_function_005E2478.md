# PspUnlockSyscallProviderExclusive

- RVA: `0x005E2478`–`0x005E24AD` (길이 `53` bytes)
- VA: `0x00000001405E2478`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E2494` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x005E249C` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x005E24A1` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PspAttachProcessToSyscallProvider](../../page/77/PspAttachProcessToSyscallProvider_function_0077E36C.md) at `0x0077E3E1`
- [PspDetachProcessFromSyscallProvider](../../page/77/PspDetachProcessFromSyscallProvider_function_0077E4BC.md) at `0x0077E4F8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E2478  40 53                           push rbx
005E247A  48 83 EC 20                     sub rsp, 0x20
005E247E  48 8D 59 40                     lea rbx, [rcx + 0x40]
005E2482  48 83 C8 FF                     or rax, 0xffffffffffffffff
005E2486  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
005E248B  24 06                           and al, 6
005E248D  3C 02                           cmp al, 2
005E248F  75 08                           jne 0x1405e2499
005E2491  48 8B CB                        mov rcx, rbx
005E2494  E8 37 39 C8 FF                  call 0x140265dd0
005E2499  48 8B CB                        mov rcx, rbx
005E249C  E8 5F F1 CF FF                  call 0x1402e1600
005E24A1  E8 0A B4 C7 FF                  call 0x14025d8b0
005E24A6  48 83 C4 20                     add rsp, 0x20
005E24AA  5B                              pop rbx
005E24AB  C3                              ret
005E24AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspUnlockSyscallProviderExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 64;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 64, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 64, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspUnlockSyscallProviderExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 64;
        result = ExfTryToWakePushLock(Arg1, a2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 64, a2, a3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 64, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E2478&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E2478[BB_005E2478]
  bb_005E2491[BB_005E2491]
  bb_005E2499[BB_005E2499]
  bb_005E24AC[BB_005E24AC]
  bb_005E2478 -->|branch| bb_005E2499
  bb_005E2478 -->|fallthrough| bb_005E2491
  bb_005E2491 -->|flow| bb_005E2499
```
