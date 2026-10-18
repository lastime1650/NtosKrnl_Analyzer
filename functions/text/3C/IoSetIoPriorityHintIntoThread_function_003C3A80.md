# IoSetIoPriorityHintIntoThread

- RVA: `0x003C3A80`–`0x003C3A9D` (길이 `29` bytes)
- VA: `0x00000001403C3A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003C3A89` → [PsSetIoPriorityThread](PsSetIoPriorityThread_function_003C3FBC.md) (function, `0x003C3FBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C3A80  48 83 EC 28                     sub rsp, 0x28
003C3A84  83 FA 05                        cmp edx, 5
003C3A87  73 0D                           jae 0x1403c3a96
003C3A89  E8 2E 05 00 00                  call 0x1403c3fbc
003C3A8E  33 C0                           xor eax, eax
003C3A90  48 83 C4 28                     add rsp, 0x28
003C3A94  C3                              ret
003C3A95  CC                              int3
003C3A96  B8 0D 00 00 C0                  mov eax, 0xc000000d
003C3A9B  EB F3                           jmp 0x1403c3a90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetIoPriorityHintIntoThread(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 >= 5) goto loc_003C3A96;
    result = PsSetIoPriorityThread(a1, a2, a3, a4);
    result = 0;
loc_003C3A90:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003C3A96:
    goto loc_003C3A90;
}
```

## 5. (Beta) C Style

```c
int64_t IoSetIoPriorityHintIntoThread(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 >= 5) goto loc_003C3A96;
    result = PsSetIoPriorityThread(Arg1, Arg2, a3, a4);
    result = 0;
loc_003C3A90:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003C3A96:
    goto loc_003C3A90;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C3A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C3A80[BB_003C3A80]
  bb_003C3A89[BB_003C3A89]
  bb_003C3A90[BB_003C3A90]
  bb_003C3A95[BB_003C3A95]
  bb_003C3A96[BB_003C3A96]
  bb_003C3A80 -->|branch| bb_003C3A96
  bb_003C3A80 -->|fallthrough| bb_003C3A89
  bb_003C3A89 -->|flow| bb_003C3A90
  bb_003C3A95 -->|flow| bb_003C3A96
  bb_003C3A96 -->|branch| bb_003C3A90
```
