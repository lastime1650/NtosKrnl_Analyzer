# sub_003972E0

- RVA: `0x003972E0`–`0x00397301` (길이 `33` bytes)
- VA: `0x00000001403972E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081334`
- 디코드: `10`개 명령, `33/33` bytes 표시
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
- `0x003972E2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003972E8` → [sub_00397328 + 0x31](Unknown_function_00397328.md) (`tail-transfer`)
  - `0x003972F9` → [KeReleaseSemaphore + 0x5A](KeReleaseSemaphore_function_00397080.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003972E0  FF C3                           inc ebx
003972E2  85 1D C4 DF C2 00               test dword ptr [rip + 0xc2dfc4], ebx
003972E8  74 6F                           je 0x140397359
003972EA  F3 90                           pause
003972EC  41 8B 07                        mov eax, dword ptr [r15]
003972EF  84 C0                           test al, al
003972F1  78 ED                           js 0x1403972e0
003972F3  F0 41 0F BA 2F 07               lock bts dword ptr [r15], 7
003972F9  0F 83 DB FD FF FF               jae 0x1403970da
003972FF  EB DF                           jmp 0x1403972e0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003972E0(void)
{
    __int64 v_rbx;

    v_rbx = (unsigned int)((v_rbx) + 1);
    if (sign_flag) goto loc_003972E0;
    goto loc_003972E0;
}
```

## 5. (Beta) C Style

```c
void sub_003972E0(void)
{
    int64_t local_rbx;

    local_rbx = (uint32_t)((local_rbx) + 1);
    if (sign_flag) goto loc_003972E0;
    goto loc_003972E0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003972E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003972E0[BB_003972E0]
  bb_003972EA[BB_003972EA]
  bb_003972F3[BB_003972F3]
  bb_003972FF[BB_003972FF]
  bb_003972E0 -->|fallthrough| bb_003972EA
  bb_003972EA -->|branch| bb_003972E0
  bb_003972EA -->|fallthrough| bb_003972F3
  bb_003972F3 -->|fallthrough| bb_003972FF
  bb_003972FF -->|branch| bb_003972E0
```
