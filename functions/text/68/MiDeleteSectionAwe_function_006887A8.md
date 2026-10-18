# MiDeleteSectionAwe

- RVA: `0x006887A8`–`0x006887CB` (길이 `35` bytes)
- VA: `0x00000001406887A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006887B5` → [MiDeleteAweInfoPages](../../page/80/MiDeleteAweInfoPages_function_0080AA40.md) (function, `0x0080AA40`)
- `0x006887BF` → [MiDeleteAweInfo](../../page/80/MiDeleteAweInfo_function_0080A9F8.md) (function, `0x0080A9F8`)

### Direct callers
- [MiDeletePageFileSectionNodes](../../page/A1/MiDeletePageFileSectionNodes_function_00A1FD50.md) at `0x00A1FDAB`
- [MiDereferenceFailedControlArea](../../page/A9/MiDereferenceFailedControlArea_function_00A99228.md) at `0x00A99255`
- [sub_00B2AD32](../../page/B2/Unknown_function_00B2AD32.md) at `0x00B2AF6E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006887B5` → [MiDeleteAweInfoPages](../../page/80/MiDeleteAweInfoPages_function_0080AA40.md) (`.text` → `PAGE`)
  - `0x006887BF` → [MiDeleteAweInfo](../../page/80/MiDeleteAweInfo_function_0080A9F8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006887A8  40 53                           push rbx
006887AA  48 83 EC 20                     sub rsp, 0x20
006887AE  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
006887B2  48 8B CB                        mov rcx, rbx
006887B5  E8 86 22 18 00                  call 0x14080aa40
006887BA  48 8B D3                        mov rdx, rbx
006887BD  33 C9                           xor ecx, ecx
006887BF  E8 34 22 18 00                  call 0x14080a9f8
006887C4  48 83 C4 20                     add rsp, 0x20
006887C8  5B                              pop rbx
006887C9  C3                              ret
006887CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteSectionAwe(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiDeleteAweInfoPages(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    a1 = 0;
    result = MiDeleteAweInfo(a1, *(unsigned __int64 *)(a1 + 8), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteSectionAwe(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiDeleteAweInfoPages(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    Arg1 = 0;
    result = MiDeleteAweInfo(Arg1, *(uint64_t *)(arg1 + 0x8), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006887A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006887A8[BB_006887A8]
  bb_006887CA[BB_006887CA]
```
