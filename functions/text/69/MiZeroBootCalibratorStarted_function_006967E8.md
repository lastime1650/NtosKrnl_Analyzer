# MiZeroBootCalibratorStarted

- RVA: `0x006967E8`–`0x00696824` (길이 `60` bytes)
- VA: `0x00000001406967E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006967FF` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00696818` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiStartZeroEngineThreads](../../page/81/MiStartZeroEngineThreads_function_00810CCC.md) at `0x00810D36`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006967E8  40 53                           push rbx
006967EA  48 83 EC 20                     sub rsp, 0x20
006967EE  48 8B D9                        mov rbx, rcx
006967F1  48 8B 89 D0 00 00 00            mov rcx, qword ptr [rcx + 0xd0]
006967F8  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
006967FF  E8 8C 1E BB FF                  call 0x140248690
00696804  48 8B 8B D0 00 00 00            mov rcx, qword ptr [rbx + 0xd0]
0069680B  8A D0                           mov dl, al
0069680D  48 81 C1 B0 3B 00 00            add rcx, 0x3bb0
00696814  C6 43 1D 00                     mov byte ptr [rbx + 0x1d], 0
00696818  E8 A3 1A BB FF                  call 0x1402482c0
0069681D  48 83 C4 20                     add rsp, 0x20
00696821  5B                              pop rbx
00696822  C3                              ret
00696823  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiZeroBootCalibratorStarted(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (*(unsigned __int64 *)(a1 + 208)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(a1 + 208)) + (0x3BB0ULL);
    *(unsigned __int8 *)(a1 + 29) = 0;
    result = MiReleaseSpinLockExclusive(a1, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiZeroBootCalibratorStarted(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (*(uint64_t *)(arg1 + 0xD0)) + (0x3BB0ULL);
    result = ExAcquireSpinLockExclusive(Arg1, a2, a3, a4);
    Arg1 = (*(uint64_t *)(arg1 + 0xD0)) + (0x3BB0ULL);
    *(uint8_t *)(arg1 + 0x1D) = 0;
    result = MiReleaseSpinLockExclusive(Arg1, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1D` | `8` | `W` |
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006967E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006967E8[BB_006967E8]
  bb_00696823[BB_00696823]
```
