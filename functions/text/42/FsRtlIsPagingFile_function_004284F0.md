# FsRtlIsPagingFile

- RVA: `0x004284F0`–`0x0042850A` (길이 `26` bytes)
- VA: `0x00000001404284F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `26/26` bytes 표시
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
004284F0  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
004284F4  48 85 C0                        test rax, rax
004284F7  74 0D                           je 0x140428506
004284F9  F6 40 06 08                     test byte ptr [rax + 6], 8
004284FD  74 07                           je 0x140428506
004284FF  B8 01 00 00 00                  mov eax, 1
00428504  C3                              ret
00428505  CC                              int3
00428506  33 C0                           xor eax, eax
00428508  C3                              ret
00428509  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlIsPagingFile(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_00428506;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 24) + 6)) & (8)) == 0) goto loc_00428506;
    return 1;
loc_00428506:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlIsPagingFile(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_00428506;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x18) + 0x6)) & (8)) == 0) goto loc_00428506;
    return 1;
loc_00428506:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004284F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004284F0[BB_004284F0]
  bb_004284F9[BB_004284F9]
  bb_004284FF[BB_004284FF]
  bb_00428505[BB_00428505]
  bb_00428506[BB_00428506]
  bb_00428509[BB_00428509]
  bb_004284F0 -->|branch| bb_00428506
  bb_004284F0 -->|fallthrough| bb_004284F9
  bb_004284F9 -->|branch| bb_00428506
  bb_004284F9 -->|fallthrough| bb_004284FF
  bb_00428505 -->|flow| bb_00428506
```
