# PopFxDeviceCriticalRegionLeave

- RVA: `0x004F1330`–`0x004F1353` (길이 `35` bytes)
- VA: `0x00000001404F1330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004F1348` → [KeLeaveGuardedRegion](../2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)

### Direct callers
- [PopFxCompleteComponentActivation](../2B/PopFxCompleteComponentActivation_function_002BDDE4.md) at `0x002BDE3D`
- [PopFxIdleWorker](../2C/PopFxIdleWorker_function_002C04A0.md) at `0x002C0548`
- [PopFxActivateComponentWorker](../2D/PopFxActivateComponentWorker_function_002D9F60.md) at `0x002D9FA4`
- [PopFxIdleWorkerTail](../43/PopFxIdleWorkerTail_function_0043CDA0.md) at `0x0043CE81`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F1330  48 83 EC 28                     sub rsp, 0x28
004F1334  44 0F 20 C0                     mov rax, cr8
004F1338  3C 02                           cmp al, 2
004F133A  73 11                           jae 0x1404f134d
004F133C  8B 81 60 03 00 00               mov eax, dword ptr [rcx + 0x360]
004F1342  0F BA E0 0C                     bt eax, 0xc
004F1346  73 05                           jae 0x1404f134d
004F1348  E8 F3 18 DF FF                  call 0x1402e2c40
004F134D  48 83 C4 28                     add rsp, 0x28
004F1351  C3                              ret
004F1352  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxDeviceCriticalRegionLeave(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_004F134D;
    result = (unsigned int)(*(unsigned int *)(a1 + 864));
    if (((unsigned __int8)(v_cr8)) < 2) {
        result = KeLeaveGuardedRegion(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxDeviceCriticalRegionLeave(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_004F134D;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x360));
    if (((uint8_t)(v_cr8)) < 2) {
        result = KeLeaveGuardedRegion(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x360` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F1330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F1330[BB_004F1330]
  bb_004F133C[BB_004F133C]
  bb_004F1348[BB_004F1348]
  bb_004F134D[BB_004F134D]
  bb_004F1352[BB_004F1352]
  bb_004F1330 -->|branch| bb_004F134D
  bb_004F1330 -->|fallthrough| bb_004F133C
  bb_004F133C -->|branch| bb_004F134D
  bb_004F133C -->|fallthrough| bb_004F1348
  bb_004F1348 -->|flow| bb_004F134D
```
