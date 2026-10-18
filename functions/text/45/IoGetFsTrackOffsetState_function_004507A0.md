# IoGetFsTrackOffsetState

- RVA: `0x004507A0`–`0x004507D9` (길이 `57` bytes)
- VA: `0x00000001404507A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `19`개 명령, `57/57` bytes 표시
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
004507A0  48 8B 81 C8 00 00 00            mov rax, qword ptr [rcx + 0xc8]
004507A7  90                              nop
004507A8  80 79 47 00                     cmp byte ptr [rcx + 0x47], 0
004507AC  7C 0B                           jl 0x1404507b9
004507AE  48 85 C0                        test rax, rax
004507B1  74 06                           je 0x1404507b9
004507B3  F6 40 02 20                     test byte ptr [rax + 2], 0x20
004507B7  75 07                           jne 0x1404507c0
004507B9  B8 25 02 00 C0                  mov eax, 0xc0000225
004507BE  C3                              ret
004507BF  CC                              int3
004507C0  48 8B 89 C8 00 00 00            mov rcx, qword ptr [rcx + 0xc8]
004507C7  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
004507CB  48 89 02                        mov qword ptr [rdx], rax
004507CE  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
004507D2  49 89 00                        mov qword ptr [r8], rax
004507D5  33 C0                           xor eax, eax
004507D7  C3                              ret
004507D8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetFsTrackOffsetState(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if ((*(unsigned __int8 *)(a1 + 71)) < 0) goto loc_004507B9;
    if (*(unsigned __int64 *)(a1 + 200) == 0) goto loc_004507B9;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 200) + 2)) & (32)) != 0) goto loc_004507C0;
loc_004507B9:
    return (unsigned int)(0xC0000225ULL);
loc_004507C0:
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 200) + 40);
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 200) + 48);
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetFsTrackOffsetState(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if ((*(uint8_t *)(arg1 + 0x47)) < 0) goto loc_004507B9;
    if (*(uint64_t *)(arg1 + 0xC8) == 0) goto loc_004507B9;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0xC8) + 0x2)) & (32)) != 0) goto loc_004507C0;
loc_004507B9:
    return (uint32_t)(0xC0000225ULL);
loc_004507C0:
    *(uint64_t *)(arg2) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC8) + 0x28);
    *(uint64_t *)(arg3) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC8) + 0x30);
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x47` | `8` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004507A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004507A0[BB_004507A0]
  bb_004507AE[BB_004507AE]
  bb_004507B3[BB_004507B3]
  bb_004507B9[BB_004507B9]
  bb_004507BF[BB_004507BF]
  bb_004507C0[BB_004507C0]
  bb_004507D8[BB_004507D8]
  bb_004507A0 -->|branch| bb_004507B9
  bb_004507A0 -->|fallthrough| bb_004507AE
  bb_004507AE -->|branch| bb_004507B9
  bb_004507AE -->|fallthrough| bb_004507B3
  bb_004507B3 -->|branch| bb_004507C0
  bb_004507B3 -->|fallthrough| bb_004507B9
  bb_004507BF -->|flow| bb_004507C0
```
