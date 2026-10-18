# sub_0020D1D0

- RVA: `0x0020D1D0`–`0x0020D1EC` (길이 `28` bytes)
- VA: `0x000000014020D1D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D950`
- 디코드: `7`개 명령, `28/28` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0020D1D3` → [sub_0020D168 + 0x1B](Unknown_function_0020D168.md) (`tail-transfer`)
  - `0x0020D1E6` → [sub_0020D579](Unknown_function_0020D579.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020D1D0  83 F9 40                        cmp ecx, 0x40
0020D1D3  77 AE                           ja 0x14020d183
0020D1D5  EB 0C                           jmp 0x14020d1e3
0020D1D7  48 8D 87 40 01 00 00            lea rax, [rdi + 0x140]
0020D1DE  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0020D1E3  45 85 C0                        test r8d, r8d
0020D1E6  0F 84 8D 03 00 00               je 0x14020d579
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020D1D0(int a1, __int64 a2, int a3)
{
    unsigned __int64 v_stack_p70;

    goto loc_0020D1E3;
loc_0020D1E3:
}
```

## 5. (Beta) C Style

```c
int64_t sub_0020D1D0(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    uint64_t v_stack_p70;

    goto loc_0020D1E3;
loc_0020D1E3:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020D1D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0020D1D0[BB_0020D1D0]
  bb_0020D1D5[BB_0020D1D5]
  bb_0020D1D7[BB_0020D1D7]
  bb_0020D1E3[BB_0020D1E3]
  bb_0020D1D0 -->|fallthrough| bb_0020D1D5
  bb_0020D1D5 -->|branch| bb_0020D1E3
  bb_0020D1D7 -->|flow| bb_0020D1E3
```
