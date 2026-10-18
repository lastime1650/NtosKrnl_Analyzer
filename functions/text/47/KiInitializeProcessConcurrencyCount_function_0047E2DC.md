# KiInitializeProcessConcurrencyCount

- RVA: `0x0047E2DC`–`0x0047E2F9` (길이 `29` bytes)
- VA: `0x000000014047E2DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeSetExpectedConcurrencyCountProcess](../5C/KeSetExpectedConcurrencyCountProcess_function_005C1AC0.md) at `0x005C1AF3`

### Static image references
- `0x0047E2DF` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047E2DC  83 21 00                        and dword ptr [rcx], 0
0047E2DF  8B 05 03 88 B4 00               mov eax, dword ptr [rip + 0xb48803]
0047E2E5  3B D0                           cmp edx, eax
0047E2E7  77 09                           ja 0x14047e2f2
0047E2E9  8B C2                           mov eax, edx
0047E2EB  C1 E0 12                        shl eax, 0x12
0047E2EE  89 01                           mov dword ptr [rcx], eax
0047E2F0  C3                              ret
0047E2F1  CC                              int3
0047E2F2  C1 E0 12                        shl eax, 0x12
0047E2F5  FF C8                           dec eax
0047E2F7  EB F5                           jmp 0x14047e2ee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInitializeProcessConcurrencyCount(__int64 a1, int a2)
{
    __int64 result;

    if (a2 > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11831299))))) goto loc_0047E2F2;
    result = (unsigned int)(((unsigned int)(a2)) << (18));
loc_0047E2EE:
    *(unsigned int *)(a1) = (unsigned int)(result);
    return result;
loc_0047E2F2:
    result = (unsigned int)((result) << (18));
    result = (unsigned int)((result) - 1);
    goto loc_0047E2EE;
}
```

## 5. (Beta) C Style

```c
int64_t KiInitializeProcessConcurrencyCount(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB48803))))) goto loc_0047E2F2;
    result = (uint32_t)(((uint32_t)(Arg2)) << (18));
loc_0047E2EE:
    *(uint32_t *)(arg1) = (uint32_t)(result);
    return result;
loc_0047E2F2:
    result = (uint32_t)((result) << (18));
    result = (uint32_t)((result) - 1);
    goto loc_0047E2EE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047E2DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047E2DC[BB_0047E2DC]
  bb_0047E2E9[BB_0047E2E9]
  bb_0047E2EE[BB_0047E2EE]
  bb_0047E2F1[BB_0047E2F1]
  bb_0047E2F2[BB_0047E2F2]
  bb_0047E2DC -->|branch| bb_0047E2F2
  bb_0047E2DC -->|fallthrough| bb_0047E2E9
  bb_0047E2E9 -->|flow| bb_0047E2EE
  bb_0047E2F1 -->|flow| bb_0047E2F2
  bb_0047E2F2 -->|branch| bb_0047E2EE
```
