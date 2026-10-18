# sub_00291CF5

- RVA: `0x00291CF5`–`0x00291D0B` (길이 `22` bytes)
- VA: `0x0000000140291CF5`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000674D0`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00291CFE` → [MiRebuildPageTableAges](../40/MiRebuildPageTableAges_function_0040D4E0.md) (function, `0x0040D4E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00291D06` → [sub_00291A10 + 0x1AD](Unknown_function_00291A10.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00291CF5  45 33 C0                        xor r8d, r8d
00291CF8  49 8B D1                        mov rdx, r9
00291CFB  48 8B CD                        mov rcx, rbp
00291CFE  E8 DD B7 17 00                  call 0x14040d4e0
00291D03  45 8B FD                        mov r15d, r13d
00291D06  E9 B2 FE FF FF                  jmp 0x140291bbd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00291CF5(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;

    a3 = 0;
    result = MiRebuildPageTableAges(v_rbp, a4, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00291CF5(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;

    Arg3 = 0;
    result = MiRebuildPageTableAges(local_rbp, Arg4, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00291CF5&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00291CF5[BB_00291CF5]
```
