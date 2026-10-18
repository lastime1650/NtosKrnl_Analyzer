# sub_00371E90

- RVA: `0x00371E90`–`0x00371EAF` (길이 `31` bytes)
- VA: `0x0000000140371E90`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A8C4`
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
- `0x00371E92` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00371E98` → [sub_00371F2D](Unknown_function_00371F2D.md) (`tail-transfer`)
  - `0x00371EA7` → [sub_00371DCB](Unknown_function_00371DCB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00371E90  FF C7                           inc edi
00371E92  85 3D 14 34 C5 00               test dword ptr [rip + 0xc53414], edi
00371E98  0F 84 8F 00 00 00               je 0x140371f2d
00371E9E  F3 90                           pause
00371EA0  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00371EA4  48 85 C0                        test rax, rax
00371EA7  0F 89 1E FF FF FF               jns 0x140371dcb
00371EAD  EB E1                           jmp 0x140371e90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00371E90(void)
{
    __int64 v_rdi;

    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_00371E90;
}
```

## 5. (Beta) C Style

```c
void sub_00371E90(void)
{
    int64_t local_rdi;

    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_00371E90;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00371E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00371E90[BB_00371E90]
  bb_00371E9E[BB_00371E9E]
  bb_00371EAD[BB_00371EAD]
  bb_00371E90 -->|fallthrough| bb_00371E9E
  bb_00371E9E -->|fallthrough| bb_00371EAD
  bb_00371EAD -->|branch| bb_00371E90
```
