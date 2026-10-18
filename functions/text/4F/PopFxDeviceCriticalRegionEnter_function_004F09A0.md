# PopFxDeviceCriticalRegionEnter

- RVA: `0x004F09A0`–`0x004F09C7` (길이 `39` bytes)
- VA: `0x00000001404F09A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopFxCompleteComponentActivation](../2B/PopFxCompleteComponentActivation_function_002BDDE4.md) at `0x002BDDFC`
- [PopFxIdleWorker](../2C/PopFxIdleWorker_function_002C04A0.md) at `0x002C04C9`
- [PopFxActivateComponentWorker](../2D/PopFxActivateComponentWorker_function_002D9F60.md) at `0x002D9F80`
- [PopFxIdleWorkerTail](../43/PopFxIdleWorkerTail_function_0043CDA0.md) at `0x0043CDD1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F09A0  44 0F 20 C0                     mov rax, cr8
004F09A4  3C 02                           cmp al, 2
004F09A6  73 1D                           jae 0x1404f09c5
004F09A8  8B 81 60 03 00 00               mov eax, dword ptr [rcx + 0x360]
004F09AE  0F BA E0 0C                     bt eax, 0xc
004F09B2  73 11                           jae 0x1404f09c5
004F09B4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F09BD  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
004F09C4  90                              nop
004F09C5  C3                              ret
004F09C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxDeviceCriticalRegionEnter(__int64 a1)
{
    __int64 result;

    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_004F09C5;
    result = (unsigned int)(*(unsigned int *)(a1 + 864));
    if (((unsigned __int8)(v_cr8)) < 2) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxDeviceCriticalRegionEnter(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (((uint8_t)(v_cr8)) >= 2) goto loc_004F09C5;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x360));
    if (((uint8_t)(v_cr8)) < 2) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x360` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F09A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F09A0[BB_004F09A0]
  bb_004F09A8[BB_004F09A8]
  bb_004F09B4[BB_004F09B4]
  bb_004F09C5[BB_004F09C5]
  bb_004F09C6[BB_004F09C6]
  bb_004F09A0 -->|branch| bb_004F09C5
  bb_004F09A0 -->|fallthrough| bb_004F09A8
  bb_004F09A8 -->|branch| bb_004F09C5
  bb_004F09A8 -->|fallthrough| bb_004F09B4
  bb_004F09B4 -->|flow| bb_004F09C5
```
