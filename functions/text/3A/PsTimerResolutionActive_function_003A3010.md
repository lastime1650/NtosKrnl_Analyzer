# PsTimerResolutionActive

- RVA: `0x003A3010`–`0x003A3030` (길이 `32` bytes)
- VA: `0x00000001403A3010`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E343`
- [KiTimerWaitTest](../23/KiTimerWaitTest_function_002337D0.md) at `0x00233940`
- [KeSetTimer2](KeSetTimer2_function_003A08E0.md) at `0x003A0F19`
- [KiExpireTimer2](KiExpireTimer2_function_003A24E0.md) at `0x003A28C6`
- [KiInitializeTimer2](KiInitializeTimer2_function_003A3288.md) at `0x003A338B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A3010  F7 81 F4 01 00 00 00 10 00 00   test dword ptr [rcx + 0x1f4], 0x1000
003A301A  75 04                           jne 0x1403a3020
003A301C  32 C0                           xor al, al
003A301E  C3                              ret
003A301F  CC                              int3
003A3020  F7 81 FC 05 00 00 00 00 00 04   test dword ptr [rcx + 0x5fc], 0x4000000
003A302A  75 F0                           jne 0x1403a301c
003A302C  B0 01                           mov al, 1
003A302E  C3                              ret
003A302F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsTimerResolutionActive(__int64 a1)
{
    __int64 result;

    if (((*(unsigned int *)(a1 + 500)) & (0x1000ULL)) != 0) goto loc_003A3020;
loc_003A301C:
    result = 0;
    return result;
loc_003A3020:
    if (((*(unsigned int *)(a1 + 1532)) & (0x4000000ULL)) != 0) goto loc_003A301C;
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t PsTimerResolutionActive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (((*(uint32_t *)(arg1 + 0x1F4)) & (0x1000ULL)) != 0) goto loc_003A3020;
loc_003A301C:
    result = 0;
    return result;
loc_003A3020:
    if (((*(uint32_t *)(arg1 + 0x5FC)) & (0x4000000ULL)) != 0) goto loc_003A301C;
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1F4` | `32` | `R` |
| `Arg1` | `+ 0x5FC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A3010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A3010[BB_003A3010]
  bb_003A301C[BB_003A301C]
  bb_003A301F[BB_003A301F]
  bb_003A3020[BB_003A3020]
  bb_003A302C[BB_003A302C]
  bb_003A302F[BB_003A302F]
  bb_003A3010 -->|branch| bb_003A3020
  bb_003A3010 -->|fallthrough| bb_003A301C
  bb_003A301F -->|flow| bb_003A3020
  bb_003A3020 -->|branch| bb_003A301C
  bb_003A3020 -->|fallthrough| bb_003A302C
```
