# BgpGxConvertRectangle

- RVA: `0x0069F190`–`0x0069F1DD` (길이 `77` bytes)
- VA: `0x000000014069F190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `25`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0069F1B4` → [BgpGxConvertRectangleEx](../46/BgpGxConvertRectangleEx_function_004696D4.md) (function, `0x004696D4`)
- `0x0069F1C2` → [BgpGxRectangleDestroy](../../pagebgfx/BC/BgpGxRectangleDestroy_function_00BC3F04.md) (function, `0x00BC3F04`)

### Direct callers
- [BgpGxProcessQrCodeBitmap](BgpGxProcessQrCodeBitmap_function_0069F244.md) at `0x0069F289`
- [BgConvertResources](../../pagebgfx/BC/BgConvertResources_function_00BC05CC.md) at `0x00BC05D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0069F1C2` → [BgpGxRectangleDestroy](../../pagebgfx/BC/BgpGxRectangleDestroy_function_00BC3F04.md) (`.text` → `PAGEBGFX`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069F190  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0069F195  57                              push rdi
0069F196  48 83 EC 20                     sub rsp, 0x20
0069F19A  48 8B D9                        mov rbx, rcx
0069F19D  33 FF                           xor edi, edi
0069F19F  48 8B 09                        mov rcx, qword ptr [rcx]
0069F1A2  39 51 08                        cmp dword ptr [rcx + 8], edx
0069F1A5  74 28                           je 0x14069f1cf
0069F1A7  48 21 7C 24 30                  and qword ptr [rsp + 0x30], rdi
0069F1AC  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0069F1B1  45 33 C9                        xor r9d, r9d
0069F1B4  E8 1B A5 DC FF                  call 0x1404696d4
0069F1B9  8B F8                           mov edi, eax
0069F1BB  85 C0                           test eax, eax
0069F1BD  78 10                           js 0x14069f1cf
0069F1BF  48 8B 0B                        mov rcx, qword ptr [rbx]
0069F1C2  E8 3D 4D 52 00                  call 0x140bc3f04
0069F1C7  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0069F1CC  48 89 0B                        mov qword ptr [rbx], rcx
0069F1CF  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0069F1D4  8B C7                           mov eax, edi
0069F1D6  48 83 C4 20                     add rsp, 0x20
0069F1DA  5F                              pop rdi
0069F1DB  C3                              ret
0069F1DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpGxConvertRectangle(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)) == a2) goto loc_0069F1CF;
    a4 = 0;
    result = BgpGxConvertRectangleEx(*(unsigned __int64 *)(a1), a2, v_stack_p8, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1);
        result = BgpGxRectangleDestroy(a1, a2, v_stack_p8, a4);
        a1 = v_stack_p8;
        *(unsigned __int64 *)(a1) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t BgpGxConvertRectangle(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)) == Arg2) goto loc_0069F1CF;
    Arg4 = 0;
    result = BgpGxConvertRectangleEx(*(uint64_t *)(arg1), Arg2, v_stack_p8, Arg4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1);
        result = BgpGxRectangleDestroy(Arg1, Arg2, v_stack_p8, Arg4);
        Arg1 = v_stack_p8;
        *(void **)(arg1) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069F190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069F190[BB_0069F190]
  bb_0069F1A7[BB_0069F1A7]
  bb_0069F1BF[BB_0069F1BF]
  bb_0069F1CF[BB_0069F1CF]
  bb_0069F1DC[BB_0069F1DC]
  bb_0069F190 -->|branch| bb_0069F1CF
  bb_0069F190 -->|fallthrough| bb_0069F1A7
  bb_0069F1A7 -->|branch| bb_0069F1CF
  bb_0069F1A7 -->|fallthrough| bb_0069F1BF
  bb_0069F1BF -->|flow| bb_0069F1CF
```
