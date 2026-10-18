# sub_00246760

- RVA: `0x00246760`–`0x00246788` (길이 `40` bytes)
- VA: `0x0000000140246760`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062074`
- 디코드: `10`개 명령, `40/40` bytes 표시
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
- `0x0024676F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00246767` → [MiUnlockProtoPoolPage + 0x23](MiUnlockProtoPoolPage_function_00246090.md) (`tail-transfer`)
  - `0x00246775` → [sub_0024682F](Unknown_function_0024682F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00246760  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00246767  0F 83 46 F9 FF FF               jae 0x1402460b3
0024676D  FF C7                           inc edi
0024676F  85 3D 37 EB D7 00               test dword ptr [rip + 0xd7eb37], edi
00246775  0F 84 B4 00 00 00               je 0x14024682f
0024677B  F3 90                           pause
0024677D  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00246781  48 85 C0                        test rax, rax
00246784  79 DA                           jns 0x140246760
00246786  EB E5                           jmp 0x14024676d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00246760(void)
{
    __int64 v_rdi;

loc_0024676D:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (!sign_flag) goto loc_00246760;
    goto loc_0024676D;
}
```

## 5. (Beta) C Style

```c
void sub_00246760(void)
{
    int64_t local_rdi;

loc_0024676D:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (!sign_flag) goto loc_00246760;
    goto loc_0024676D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00246760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00246760[BB_00246760]
  bb_0024676D[BB_0024676D]
  bb_0024677B[BB_0024677B]
  bb_00246786[BB_00246786]
  bb_00246760 -->|fallthrough| bb_0024676D
  bb_0024676D -->|fallthrough| bb_0024677B
  bb_0024677B -->|branch| bb_00246760
  bb_0024677B -->|fallthrough| bb_00246786
  bb_00246786 -->|branch| bb_0024676D
```
