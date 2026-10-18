# FsRtlAreThereWaitingFileLocks

- RVA: `0x004A0170`–`0x004A018B` (길이 `27` bytes)
- VA: `0x00000001404A0170`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `27/27` bytes 표시
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
004A0170  33 C0                           xor eax, eax
004A0172  48 85 C9                        test rcx, rcx
004A0175  74 09                           je 0x1404a0180
004A0177  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
004A017B  48 85 C9                        test rcx, rcx
004A017E  75 02                           jne 0x1404a0182
004A0180  C3                              ret
004A0181  CC                              int3
004A0182  48 39 41 30                     cmp qword ptr [rcx + 0x30], rax
004A0186  0F 95 C0                        setne al
004A0189  C3                              ret
004A018A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlAreThereWaitingFileLocks(__int64 a1)
{
    __int64 result;

    result = 0;
    if (a1 == 0) goto loc_004A0180;
    if (*(unsigned __int64 *)(a1 + 24) != 0) goto loc_004A0182;
loc_004A0180:
    return result;
loc_004A0182:
    result = ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 48)) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlAreThereWaitingFileLocks(int64_t Arg1)
{
    int64_t result;

    result = 0;
    if (Arg1 == 0) goto loc_004A0180;
    if (*(uint64_t *)(Arg1 + 0x18) != 0) goto loc_004A0182;
loc_004A0180:
    return result;
loc_004A0182:
    result = ((*(uint64_t *)(*(uint64_t *)(Arg1 + 0x18) + 0x30)) != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A0170&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A0170[BB_004A0170]
  bb_004A0177[BB_004A0177]
  bb_004A0180[BB_004A0180]
  bb_004A0181[BB_004A0181]
  bb_004A0182[BB_004A0182]
  bb_004A018A[BB_004A018A]
  bb_004A0170 -->|branch| bb_004A0180
  bb_004A0170 -->|fallthrough| bb_004A0177
  bb_004A0177 -->|branch| bb_004A0182
  bb_004A0177 -->|fallthrough| bb_004A0180
  bb_004A0181 -->|flow| bb_004A0182
```
