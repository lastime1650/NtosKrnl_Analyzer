# sub_00246120

- RVA: `0x00246120`–`0x0024613F` (길이 `31` bytes)
- VA: `0x0000000140246120`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061F00`
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
- `0x00246122` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00246128` → [sub_002461C2](Unknown_function_002461C2.md) (`tail-transfer`)
  - `0x00246137` → [MiUnlockProtoPoolPage + 0x1A](MiUnlockProtoPoolPage_function_00246090.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00246120  FF C7                           inc edi
00246122  85 3D 84 F1 D7 00               test dword ptr [rip + 0xd7f184], edi
00246128  0F 84 94 00 00 00               je 0x1402461c2
0024612E  F3 90                           pause
00246130  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00246134  48 85 C0                        test rax, rax
00246137  0F 89 6D FF FF FF               jns 0x1402460aa
0024613D  EB E1                           jmp 0x140246120
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00246120(void)
{
    __int64 v_rdi;

    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_00246120;
}
```

## 5. (Beta) C Style

```c
void sub_00246120(void)
{
    int64_t local_rdi;

    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_00246120;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00246120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00246120[BB_00246120]
  bb_0024612E[BB_0024612E]
  bb_0024613D[BB_0024613D]
  bb_00246120 -->|fallthrough| bb_0024612E
  bb_0024612E -->|fallthrough| bb_0024613D
  bb_0024613D -->|branch| bb_00246120
```
