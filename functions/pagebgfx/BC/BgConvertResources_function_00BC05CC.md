# BgConvertResources

- RVA: `0x00BC05CC`–`0x00BC05E4` (길이 `24` bytes)
- VA: `0x0000000140BC05CC`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BC05D9` → [BgpGxConvertRectangle](../../text/69/BgpGxConvertRectangle_function_0069F190.md) (function, `0x0069F190`)

### Direct callers
- [BgkSetVirtualFrameBuffer](../../text/59/BgkSetVirtualFrameBuffer_function_00590F50.md) at `0x005910F3`

### Static image references
- `0x00BC05D2` → RVA `0x00EF04D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC05D9` → [BgpGxConvertRectangle](../../text/69/BgpGxConvertRectangle_function_0069F190.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC05CC  48 83 EC 28                     sub rsp, 0x28
00BC05D0  8B D1                           mov edx, ecx
00BC05D2  48 8D 0D FF FE 32 00            lea rcx, [rip + 0x32feff]
00BC05D9  E8 B2 EB AD FF                  call 0x14069f190
00BC05DE  48 83 C4 28                     add rsp, 0x28
00BC05E2  C3                              ret
00BC05E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgConvertResources(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = BgpGxConvertRectangle(v_rip + 3342079, (unsigned int)(a1), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BgConvertResources(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = BgpGxConvertRectangle(v_rip + 3342079, (uint32_t)(Arg1), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC05CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC05CC[BB_00BC05CC]
  bb_00BC05E3[BB_00BC05E3]
```
