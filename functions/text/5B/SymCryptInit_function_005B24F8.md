# SymCryptInit

- RVA: `0x005B24F8`–`0x005B250C` (길이 `20` bytes)
- VA: `0x00000001405B24F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B2501` → [SymCryptInitEnvWindowsKernelmodeWin8_1nLater](../51/SymCryptInitEnvWindowsKernelmodeWin8_1nLater_function_0051C948.md) (function, `0x0051C948`)

### Direct callers
- [HvInitializeHashLibrary](../../page/7E/HvInitializeHashLibrary_function_007EDC44.md) at `0x007EDC48`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B24F8  48 83 EC 28                     sub rsp, 0x28
005B24FC  B9 0C 00 67 00                  mov ecx, 0x67000c
005B2501  E8 42 A4 F6 FF                  call 0x14051c948
005B2506  48 83 C4 28                     add rsp, 0x28
005B250A  C3                              ret
005B250B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptInit(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptInitEnvWindowsKernelmodeWin8_1nLater((unsigned int)(0x67000CULL), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SymCryptInit(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptInitEnvWindowsKernelmodeWin8_1nLater((uint32_t)(0x67000CULL), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B24F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B24F8[BB_005B24F8]
  bb_005B250B[BB_005B250B]
```
