# sub_002C1CF0

- RVA: `0x002C1CF0`–`0x002C1D11` (길이 `33` bytes)
- VA: `0x00000001402C1CF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E7A4`
- 디코드: `8`개 명령, `33/33` bytes 표시
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
- `0x002C1CF3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002C1CFA` → [sub_002C1E2F](Unknown_function_002C1E2F.md) (`tail-transfer`)
  - `0x002C1D09` → [sub_002C1B47 + 0x25](Unknown_function_002C1B47.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C1CF0  41 FF C4                        inc r12d
002C1CF3  44 85 25 B2 35 D0 00            test dword ptr [rip + 0xd035b2], r12d
002C1CFA  0F 84 2F 01 00 00               je 0x1402c1e2f
002C1D00  F3 90                           pause
002C1D02  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002C1D06  48 85 C0                        test rax, rax
002C1D09  0F 89 5D FE FF FF               jns 0x1402c1b6c
002C1D0F  EB DF                           jmp 0x1402c1cf0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C1CF0(void)
{
    __int64 v_r12;

    v_r12 = (unsigned int)((v_r12) + 1);
    goto loc_002C1CF0;
}
```

## 5. (Beta) C Style

```c
void sub_002C1CF0(void)
{
    int64_t local_r12;

    local_r12 = (uint32_t)((local_r12) + 1);
    goto loc_002C1CF0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C1CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C1CF0[BB_002C1CF0]
  bb_002C1D00[BB_002C1D00]
  bb_002C1D0F[BB_002C1D0F]
  bb_002C1CF0 -->|fallthrough| bb_002C1D00
  bb_002C1D00 -->|fallthrough| bb_002C1D0F
  bb_002C1D0F -->|branch| bb_002C1CF0
```
