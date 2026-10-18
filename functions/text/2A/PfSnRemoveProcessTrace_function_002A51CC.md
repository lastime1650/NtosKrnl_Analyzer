# PfSnRemoveProcessTrace

- RVA: `0x002A51CC`–`0x002A5217` (길이 `75` bytes)
- VA: `0x00000001402A51CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002A51EE` → [ExReleaseRundownProtectionEx](ExReleaseRundownProtectionEx_function_002A55B0.md) (function, `0x002A55B0`)
- `0x002A51FA` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002A5208` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PfSnDeactivateTrace](PfSnDeactivateTrace_function_002A50CC.md) at `0x002A5109`

### Static image references
- `0x002A51F3` → RVA `0x00E67260` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A51CC  40 53                           push rbx
002A51CE  48 83 EC 20                     sub rsp, 0x20
002A51D2  33 D2                           xor edx, edx
002A51D4  48 87 91 90 03 00 00            xchg qword ptr [rcx + 0x390], rdx
002A51DB  48 8B DA                        mov rbx, rdx
002A51DE  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
002A51E2  83 E2 0F                        and edx, 0xf
002A51E5  76 0C                           jbe 0x1402a51f3
002A51E7  48 8D 8B 68 01 00 00            lea rcx, [rbx + 0x168]
002A51EE  E8 BD 03 00 00                  call 0x1402a55b0
002A51F3  48 8D 0D 66 20 BC 00            lea rcx, [rip + 0xbc2066]
002A51FA  E8 71 32 F6 FF                  call 0x140208470
002A51FF  8A D0                           mov dl, al
002A5201  48 8D 0D 58 20 BC 00            lea rcx, [rip + 0xbc2058]
002A5208  E8 93 D9 0E 00                  call 0x140392ba0
002A520D  48 8B C3                        mov rax, rbx
002A5210  48 83 C4 20                     add rsp, 0x20
002A5214  5B                              pop rbx
002A5215  C3                              ret
002A5216  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnRemoveProcessTrace(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    v_rbx = (0) & (-16);
    a2 = (unsigned int)((a2) & (15));
    if (!(condition_is_below_or_equal)) {
        a1 = v_rbx + 360;
        result = ExReleaseRundownProtectionEx(a1, a2, a3, a4);
    }
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12329062, a2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 12329048, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnRemoveProcessTrace(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    local_rbx = (0) & (-16);
    Arg2 = (uint32_t)((Arg2) & (15));
    if (!(condition_is_below_or_equal)) {
        Arg1 = local_rbx + 360;
        result = ExReleaseRundownProtectionEx(Arg1, Arg2, a3, a4);
    }
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 12329062, Arg2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 12329048, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x390` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A51CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A51CC[BB_002A51CC]
  bb_002A51E7[BB_002A51E7]
  bb_002A51F3[BB_002A51F3]
  bb_002A5216[BB_002A5216]
  bb_002A51CC -->|branch| bb_002A51F3
  bb_002A51CC -->|fallthrough| bb_002A51E7
  bb_002A51E7 -->|flow| bb_002A51F3
```
