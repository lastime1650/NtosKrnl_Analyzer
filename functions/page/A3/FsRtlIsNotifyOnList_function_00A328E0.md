# FsRtlIsNotifyOnList

- RVA: `0x00A328E0`–`0x00A328FF` (길이 `31` bytes)
- VA: `0x0000000140A328E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlNotifyCleanup](FsRtlNotifyCleanup_function_00A32840.md) at `0x00A32882`
- [FsRtlNotifyFilterChangeDirectory](../AA/FsRtlNotifyFilterChangeDirectory_function_00AAB9E0.md) at `0x00AABAA4`
- [FsRtlNotifyFilterChangeDirectoryLite](../AD/FsRtlNotifyFilterChangeDirectoryLite_function_00ADC950.md) at `0x00ADCA39`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A328E0  48 8B 01                        mov rax, qword ptr [rcx]
00A328E3  45 33 C0                        xor r8d, r8d
00A328E6  48 3B C1                        cmp rax, rcx
00A328E9  74 0F                           je 0x140a328fa
00A328EB  48 39 50 E8                     cmp qword ptr [rax - 0x18], rdx
00A328EF  74 05                           je 0x140a328f6
00A328F1  48 8B 00                        mov rax, qword ptr [rax]
00A328F4  EB F0                           jmp 0x140a328e6
00A328F6  4C 8D 40 E0                     lea r8, [rax - 0x20]
00A328FA  49 8B C0                        mov rax, r8
00A328FD  C3                              ret
00A328FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlIsNotifyOnList(__int64 a1, __int64 a2, int a3)
{
    a3 = 0;
loc_00A328E6:
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_00A328FA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) - 24)) == a2) goto loc_00A328F6;
    goto loc_00A328E6;
loc_00A328F6:
loc_00A328FA:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) - 32;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlIsNotifyOnList(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg3 = 0;
loc_00A328E6:
    if ((*(uint64_t *)(arg1)) == Arg1) goto loc_00A328FA;
    if ((*(uint64_t *)(*(uint64_t *)(arg1) - 0x18)) == Arg2) goto loc_00A328F6;
    goto loc_00A328E6;
loc_00A328F6:
loc_00A328FA:
    return *(uint64_t *)(*(uint64_t *)(arg1)) - 32;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A328E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A328E0[BB_00A328E0]
  bb_00A328E6[BB_00A328E6]
  bb_00A328EB[BB_00A328EB]
  bb_00A328F1[BB_00A328F1]
  bb_00A328F6[BB_00A328F6]
  bb_00A328FA[BB_00A328FA]
  bb_00A328FE[BB_00A328FE]
  bb_00A328E0 -->|flow| bb_00A328E6
  bb_00A328E6 -->|branch| bb_00A328FA
  bb_00A328E6 -->|fallthrough| bb_00A328EB
  bb_00A328EB -->|branch| bb_00A328F6
  bb_00A328EB -->|fallthrough| bb_00A328F1
  bb_00A328F1 -->|branch| bb_00A328E6
  bb_00A328F6 -->|flow| bb_00A328FA
```
