# MiRestockOverCommit

- RVA: `0x00407D94`–`0x00407DBC` (길이 `40` bytes)
- VA: `0x0000000140407D94`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00245F1D](../24/Unknown_function_00245F1D.md) at `0x00245F40`
- [sub_002467B9](../24/Unknown_function_002467B9.md) at `0x002467D7`
- [sub_00246C9F](../24/Unknown_function_00246C9F.md) at `0x00246CC7`
- [sub_002484B4](../24/Unknown_function_002484B4.md) at `0x0024860C`
- [MiAddPageToInsertList](../24/MiAddPageToInsertList_function_0024A950.md) at `0x0024AD85`
- [sub_00285DC9](../28/Unknown_function_00285DC9.md) at `0x00285DE6`
- [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) at `0x00322C0B`
- [sub_0033EABD](../33/Unknown_function_0033EABD.md) at `0x0033ED98`
- [MiReleaseWriteInProgressCharges](MiReleaseWriteInProgressCharges_function_00407B4C.md) at `0x00407CD9`
- [sub_004084EC](Unknown_function_004084EC.md) at `0x00408509`
- [MiIncreaseCommitLimits](../68/MiIncreaseCommitLimits_function_0068CADC.md) at `0x0068CB4C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00407D94  4C 8B 81 08 42 00 00            mov r8, qword ptr [rcx + 0x4208]
00407D9B  4D 85 C0                        test r8, r8
00407D9E  74 17                           je 0x140407db7
00407DA0  49 3B D0                        cmp rdx, r8
00407DA3  48 8B C2                        mov rax, rdx
00407DA6  49 0F 47 C0                     cmova rax, r8
00407DAA  4C 2B C0                        sub r8, rax
00407DAD  4C 89 81 08 42 00 00            mov qword ptr [rcx + 0x4208], r8
00407DB4  48 2B D0                        sub rdx, rax
00407DB7  48 8B C2                        mov rax, rdx
00407DBA  C3                              ret
00407DBB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRestockOverCommit(__int64 a1, __int64 a2)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 16904) != 0) {
        result = a2;
        if (a2 > (*(unsigned __int64 *)(a1 + 16904))) { result = *(unsigned __int64 *)(a1 + 16904); }
        a3 = (*(unsigned __int64 *)(a1 + 16904)) - (result);
        *(unsigned __int64 *)(a1 + 16904) = a3;
        a2 = (a2) - (result);
    }
    return a2;
}
```

## 5. (Beta) C Style

```c
int64_t MiRestockOverCommit(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x4208) != 0) {
        result = Arg2;
        if (Arg2 > (*(uint64_t *)(arg1 + 0x4208))) { result = *(uint64_t *)(arg1 + 0x4208); }
        a3 = (*(uint64_t *)(arg1 + 0x4208)) - (result);
        *(uint64_t *)(arg1 + 0x4208) = a3;
        Arg2 = (Arg2) - (result);
    }
    return Arg2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4208` | `64` | `R` |
| `Arg1` | `+ 0x4208` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00407D94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00407D94[BB_00407D94]
  bb_00407DA0[BB_00407DA0]
  bb_00407DB7[BB_00407DB7]
  bb_00407DBB[BB_00407DBB]
  bb_00407D94 -->|branch| bb_00407DB7
  bb_00407D94 -->|fallthrough| bb_00407DA0
  bb_00407DA0 -->|flow| bb_00407DB7
```
