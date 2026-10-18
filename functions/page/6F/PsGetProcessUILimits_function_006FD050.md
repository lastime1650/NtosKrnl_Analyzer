# PsGetProcessUILimits

- RVA: `0x006FD050`–`0x006FD07C` (길이 `44` bytes)
- VA: `0x00000001406FD050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006FD050  48 8B 91 A0 02 00 00            mov rdx, qword ptr [rcx + 0x2a0]
006FD057  33 C0                           xor eax, eax
006FD059  EB 1A                           jmp 0x1406fd075
006FD05B  8B 8A 10 06 00 00               mov ecx, dword ptr [rdx + 0x610]
006FD061  F6 C1 10                        test cl, 0x10
006FD064  74 08                           je 0x1406fd06e
006FD066  8B 8A 20 02 00 00               mov ecx, dword ptr [rdx + 0x220]
006FD06C  0B C1                           or eax, ecx
006FD06E  48 8B 92 18 05 00 00            mov rdx, qword ptr [rdx + 0x518]
006FD075  48 85 D2                        test rdx, rdx
006FD078  75 E1                           jne 0x1406fd05b
006FD07A  C3                              ret
006FD07B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetProcessUILimits(__int64 a1)
{
    __int64 result;

    result = 0;
    goto loc_006FD075;
loc_006FD05B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 672) + 1552)))) & (16)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 672) + 544);
        result = (unsigned int)((result) | ((unsigned int)(a1)));
    }
loc_006FD075:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 672) + 1304) != 0) goto loc_006FD05B;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetProcessUILimits(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    goto loc_006FD075;
loc_006FD05B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x610)))) & (16)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x220);
        result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    }
loc_006FD075:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x518) != 0) goto loc_006FD05B;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2A0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x006FD050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FD050[BB_006FD050]
  bb_006FD05B[BB_006FD05B]
  bb_006FD066[BB_006FD066]
  bb_006FD06E[BB_006FD06E]
  bb_006FD075[BB_006FD075]
  bb_006FD07A[BB_006FD07A]
  bb_006FD07B[BB_006FD07B]
  bb_006FD050 -->|branch| bb_006FD075
  bb_006FD05B -->|branch| bb_006FD06E
  bb_006FD05B -->|fallthrough| bb_006FD066
  bb_006FD066 -->|flow| bb_006FD06E
  bb_006FD06E -->|flow| bb_006FD075
  bb_006FD075 -->|branch| bb_006FD05B
  bb_006FD075 -->|fallthrough| bb_006FD07A
```
