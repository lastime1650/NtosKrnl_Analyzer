# MiImageSuitableForSystem

- RVA: `0x00AAC408`–`0x00AAC436` (길이 `46` bytes)
- VA: `0x0000000140AAC408`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00B40C48](../B4/Unknown_function_00B40C48.md) at `0x00B4100B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAC408  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00AAC40C  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00AAC410  48 83 78 20 00                  cmp qword ptr [rax + 0x20], 0
00AAC415  74 18                           je 0x140aac42f
00AAC417  C7 02 01 00 00 00               mov dword ptr [rdx], 1
00AAC41D  F7 41 38 00 00 00 20            test dword ptr [rcx + 0x38], 0x20000000
00AAC424  74 0C                           je 0x140aac432
00AAC426  48 8B 01                        mov rax, qword ptr [rcx]
00AAC429  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00AAC42D  C3                              ret
00AAC42E  CC                              int3
00AAC42F  83 22 00                        and dword ptr [rdx], 0
00AAC432  33 C0                           xor eax, eax
00AAC434  C3                              ret
00AAC435  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiImageSuitableForSystem(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (*(unsigned __int64 *)(a1 + 96)) & (-8);
    if ((*(unsigned __int64 *)(result + 32)) == 0) goto loc_00AAC42F;
    *(unsigned int *)(a2) = 1;
    if (((*(unsigned int *)(a1 + 56)) & (0x20000000ULL)) == 0) goto loc_00AAC432;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32);
loc_00AAC42F:
loc_00AAC432:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiImageSuitableForSystem(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (*(uint64_t *)(arg1 + 0x60)) & (-8);
    if ((*(uint64_t *)(result + 0x20)) == 0) goto loc_00AAC42F;
    *(uint32_t *)(arg2) = 1;
    if (((*(uint32_t *)(arg1 + 0x38)) & (0x20000000ULL)) == 0) goto loc_00AAC432;
    return *(uint64_t *)(*(uint64_t *)(arg1) + 0x20);
loc_00AAC42F:
loc_00AAC432:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAC408&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAC408[BB_00AAC408]
  bb_00AAC417[BB_00AAC417]
  bb_00AAC426[BB_00AAC426]
  bb_00AAC42E[BB_00AAC42E]
  bb_00AAC42F[BB_00AAC42F]
  bb_00AAC432[BB_00AAC432]
  bb_00AAC435[BB_00AAC435]
  bb_00AAC408 -->|branch| bb_00AAC42F
  bb_00AAC408 -->|fallthrough| bb_00AAC417
  bb_00AAC417 -->|branch| bb_00AAC432
  bb_00AAC417 -->|fallthrough| bb_00AAC426
  bb_00AAC42E -->|flow| bb_00AAC42F
  bb_00AAC42F -->|flow| bb_00AAC432
```
