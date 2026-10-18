# sub_0023EB60

- RVA: `0x0023EB60`–`0x0023EB7F` (길이 `31` bytes)
- VA: `0x000000014023EB60`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061474`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0023EB62` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0023EB68` → [sub_0023EBEE](Unknown_function_0023EBEE.md) (`tail-transfer`)
  - `0x0023EB7A` → [sub_0023E99F + 0x4E](Unknown_function_0023E99F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023EB60  FF C5                           inc ebp
0023EB62  85 2D 44 67 D8 00               test dword ptr [rip + 0xd86744], ebp
0023EB68  0F 84 80 00 00 00               je 0x14023ebee
0023EB6E  F3 90                           pause
0023EB70  48 8B 1E                        mov rbx, qword ptr [rsi]
0023EB73  48 0F BA E3 3C                  bt rbx, 0x3c
0023EB78  72 E6                           jb 0x14023eb60
0023EB7A  E9 6E FE FF FF                  jmp 0x14023e9ed
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0023EB60(void)
{
    __int64 v_rbp;

    v_rbp = (unsigned int)((v_rbp) + 1);
    if (condition_is_below) goto loc_0023EB60;
}
```

## 5. (Beta) C Style

```c
void sub_0023EB60(void)
{
    int64_t local_rbp;

    local_rbp = (uint32_t)((local_rbp) + 1);
    if (condition_is_below) goto loc_0023EB60;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023EB60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023EB60[BB_0023EB60]
  bb_0023EB6E[BB_0023EB6E]
  bb_0023EB7A[BB_0023EB7A]
  bb_0023EB60 -->|fallthrough| bb_0023EB6E
  bb_0023EB6E -->|branch| bb_0023EB60
  bb_0023EB6E -->|fallthrough| bb_0023EB7A
```
