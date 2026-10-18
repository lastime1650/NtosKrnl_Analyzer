# sub_003455E0

- RVA: `0x003455E0`–`0x00345601` (길이 `33` bytes)
- VA: `0x00000001403455E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077F14`
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
- `0x003455E3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003455EA` → [sub_0034569C](Unknown_function_0034569C.md) (`tail-transfer`)
  - `0x003455F9` → [sub_00345517](Unknown_function_00345517.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003455E0  41 FF C7                        inc r15d
003455E3  44 85 3D C2 FC C7 00            test dword ptr [rip + 0xc7fcc2], r15d
003455EA  0F 84 AC 00 00 00               je 0x14034569c
003455F0  F3 90                           pause
003455F2  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003455F6  48 85 C0                        test rax, rax
003455F9  0F 89 18 FF FF FF               jns 0x140345517
003455FF  EB DF                           jmp 0x1403455e0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003455E0(void)
{
    __int64 v_r15;

    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_003455E0;
}
```

## 5. (Beta) C Style

```c
void sub_003455E0(void)
{
    int64_t local_r15;

    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_003455E0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003455E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003455E0[BB_003455E0]
  bb_003455F0[BB_003455F0]
  bb_003455FF[BB_003455FF]
  bb_003455E0 -->|fallthrough| bb_003455F0
  bb_003455F0 -->|fallthrough| bb_003455FF
  bb_003455FF -->|branch| bb_003455E0
```
