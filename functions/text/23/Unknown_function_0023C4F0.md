# sub_0023C4F0

- RVA: `0x0023C4F0`–`0x0023C50F` (길이 `31` bytes)
- VA: `0x000000014023C4F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060EDC`
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
- `0x0023C4F2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0023C4F8` → [sub_0023C6BE](Unknown_function_0023C6BE.md) (`tail-transfer`)
  - `0x0023C507` → [sub_0023C21A + 0x44](Unknown_function_0023C21A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0023C4F0  FF C5                           inc ebp
0023C4F2  85 2D B4 8D D8 00               test dword ptr [rip + 0xd88db4], ebp
0023C4F8  0F 84 C0 01 00 00               je 0x14023c6be
0023C4FE  F3 90                           pause
0023C500  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0023C504  48 85 C0                        test rax, rax
0023C507  0F 89 51 FD FF FF               jns 0x14023c25e
0023C50D  EB E1                           jmp 0x14023c4f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0023C4F0(void)
{
    __int64 v_rbp;

    v_rbp = (unsigned int)((v_rbp) + 1);
    goto loc_0023C4F0;
}
```

## 5. (Beta) C Style

```c
void sub_0023C4F0(void)
{
    int64_t local_rbp;

    local_rbp = (uint32_t)((local_rbp) + 1);
    goto loc_0023C4F0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023C4F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0023C4F0[BB_0023C4F0]
  bb_0023C4FE[BB_0023C4FE]
  bb_0023C50D[BB_0023C50D]
  bb_0023C4F0 -->|fallthrough| bb_0023C4FE
  bb_0023C4FE -->|fallthrough| bb_0023C50D
  bb_0023C50D -->|branch| bb_0023C4F0
```
