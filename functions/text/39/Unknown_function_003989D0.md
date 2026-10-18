# sub_003989D0

- RVA: `0x003989D0`–`0x003989EB` (길이 `27` bytes)
- VA: `0x00000001403989D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000815A8`
- 디코드: `8`개 명령, `27/27` bytes 표시
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
- `0x003989D2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003989D8` → [sub_00398A1B](Unknown_function_00398A1B.md) (`tail-transfer`)
  - `0x003989E3` → [sub_003988DA + 0x16](Unknown_function_003988DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003989D0  FF C6                           inc esi
003989D2  85 35 D4 C8 C2 00               test dword ptr [rip + 0xc2c8d4], esi
003989D8  74 41                           je 0x140398a1b
003989DA  F3 90                           pause
003989DC  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003989E0  48 85 C0                        test rax, rax
003989E3  0F 84 07 FF FF FF               je 0x1403988f0
003989E9  EB E5                           jmp 0x1403989d0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003989D0(void)
{
    __int64 v_rsi;

    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_003989D0;
}
```

## 5. (Beta) C Style

```c
void sub_003989D0(void)
{
    int64_t local_rsi;

    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_003989D0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003989D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003989D0[BB_003989D0]
  bb_003989DA[BB_003989DA]
  bb_003989E9[BB_003989E9]
  bb_003989D0 -->|fallthrough| bb_003989DA
  bb_003989DA -->|fallthrough| bb_003989E9
  bb_003989E9 -->|branch| bb_003989D0
```
