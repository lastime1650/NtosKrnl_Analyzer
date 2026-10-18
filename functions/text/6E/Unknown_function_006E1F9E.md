# sub_006E1F9E

- RVA: `0x006E1F9E`–`0x006E1FAB` (길이 `13` bytes)
- VA: `0x00000001406E1F9E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000769B8`
- 디코드: `4`개 명령, `13/13` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E1FA6` → [MiCoalesceFreeSmallPages + 0x5AA](../33/MiCoalesceFreeSmallPages_function_00336340.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1F9E  41 8B C0                        mov eax, r8d
006E1FA1  F7 D0                           not eax
006E1FA3  83 E0 01                        and eax, 1
006E1FA6  E9 3F 49 C5 FF                  jmp 0x1403368ea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E1F9E(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    result = (unsigned int)(~((unsigned int)(a3)));
    result = (unsigned int)((result) & (1));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E1F9E(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    result = (uint32_t)(~((uint32_t)(Arg3)));
    result = (uint32_t)((result) & (1));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1F9E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1F9E[BB_006E1F9E]
```
