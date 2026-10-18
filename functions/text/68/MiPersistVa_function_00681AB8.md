# MiPersistVa

- RVA: `0x00681AB8`–`0x00681AD5` (길이 `29` bytes)
- VA: `0x0000000140681AB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00681ACA` → [MiPersistMemory](MiPersistMemory_function_00681A40.md) (function, `0x00681A40`)

### Direct callers
- [MiPersistMdl](../40/MiPersistMdl_function_00402B2C.md) at `0x00402BD8`
- [MiCopyFilePage](MiCopyFilePage_function_00680790.md) at `0x00680810`
- [MiPersistPage](MiPersistPage_function_00681A68.md) at `0x00681A92`

### Static image references
- `0x00681ABC` → RVA `0x00E2DC40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00681AB8  48 83 EC 28                     sub rsp, 0x28
00681ABC  80 3D 7D C1 7A 00 00            cmp byte ptr [rip + 0x7ac17d], 0
00681AC3  75 0A                           jne 0x140681acf
00681AC5  BA 00 10 00 00                  mov edx, 0x1000
00681ACA  E8 71 FF FF FF                  call 0x140681a40
00681ACF  48 83 C4 28                     add rsp, 0x28
00681AD3  C3                              ret
00681AD4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPersistVa(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 8044925)) == 0) {
        a2 = 0x1000ULL;
        result = MiPersistMemory(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiPersistVa(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x7AC17D)) == 0) {
        a2 = 0x1000ULL;
        result = MiPersistMemory(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00681AB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00681AB8[BB_00681AB8]
  bb_00681AC5[BB_00681AC5]
  bb_00681ACF[BB_00681ACF]
  bb_00681AD4[BB_00681AD4]
  bb_00681AB8 -->|branch| bb_00681ACF
  bb_00681AB8 -->|fallthrough| bb_00681AC5
  bb_00681AC5 -->|flow| bb_00681ACF
```
