# MiStoreReleaseReservedPageCharges

- RVA: `0x00693054`–`0x0069308D` (길이 `57` bytes)
- VA: `0x0000000140693054`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00693062` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0069306E` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00693081` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiStoreDeletePartition](MiStoreDeletePartition_function_006926F4.md) at `0x0069282C`
- [MmStoreRegister](../../page/80/MmStoreRegister_function_0080E6D8.md) at `0x0080E8ED`

### Static image references
- `0x00693067` → RVA `0x00E30040` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00693054  40 53                           push rbx
00693056  48 83 EC 20                     sub rsp, 0x20
0069305A  BA 20 00 00 00                  mov edx, 0x20
0069305F  48 8B D9                        mov rbx, rcx
00693062  E8 35 F9 C8 FF                  call 0x14032299c
00693067  48 8D 0D D2 CF 79 00            lea rcx, [rip + 0x79cfd2]
0069306E  E8 1D 56 BB FF                  call 0x140248690
00693073  F0 83 63 04 FB                  lock and dword ptr [rbx + 4], 0xfffffffb
00693078  8A D0                           mov dl, al
0069307A  48 8D 0D BF CF 79 00            lea rcx, [rip + 0x79cfbf]
00693081  E8 3A 52 BB FF                  call 0x1402482c0
00693086  48 83 C4 20                     add rsp, 0x20
0069308A  5B                              pop rbx
0069308B  C3                              ret
0069308C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreReleaseReservedPageCharges(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiReleaseNonPagedResources(a1, 32, a3, a4);
    result = ExAcquireSpinLockExclusive(v_rip + 7983058, 32, a3, a4);
    result = MiReleaseSpinLockExclusive(v_rip + 7983039, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreReleaseReservedPageCharges(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiReleaseNonPagedResources(Arg1, 32, a3, a4);
    result = ExAcquireSpinLockExclusive(v_rip + 7983058, 32, a3, a4);
    result = MiReleaseSpinLockExclusive(v_rip + 7983039, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00693054&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00693054[BB_00693054]
  bb_0069308C[BB_0069308C]
```
