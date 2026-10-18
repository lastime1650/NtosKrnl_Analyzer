# sub_00238DA4

- RVA: `0x00238DA4`–`0x00238DB5` (길이 `17` bytes)
- VA: `0x0000000140238DA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060B50`
- 디코드: `3`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00238DAB` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00238DA4` → RVA `0x00E2F3B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00238DB0` → [sub_00238945](Unknown_function_00238945.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00238DA4  48 8D 0D 0D 66 BF 00            lea rcx, [rip + 0xbf660d]
00238DAB  E8 E0 F8 00 00                  call 0x140248690
00238DB0  E9 90 FB FF FF                  jmp 0x140238945
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00238DA4(void)
{
    __int64 result;

    result = ExAcquireSpinLockExclusive(v_rip + 12543501, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00238DA4(void)
{
    int64_t result;

    result = ExAcquireSpinLockExclusive(v_rip + 12543501, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00238DA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00238DA4[BB_00238DA4]
```
