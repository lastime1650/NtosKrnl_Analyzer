# XpressDecodeCreate

- RVA: `0x006A8AB4`–`0x006A8AD6` (길이 `34` bytes)
- VA: `0x00000001406A8AB4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A8ABF` → [CMFAllocFn](../../page/7D/CMFAllocFn_function_007D2890.md) (function, `0x007D2890`)

### Direct callers
- [CMFReadCompressedSegment](../../page/7D/CMFReadCompressedSegment_function_007D3580.md) at `0x007D3608`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006A8ABF` → [CMFAllocFn](../../page/7D/CMFAllocFn_function_007D2890.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A8AB4  48 83 EC 28                     sub rsp, 0x28
006A8AB8  BA 70 00 00 00                  mov edx, 0x70
006A8ABD  33 C9                           xor ecx, ecx
006A8ABF  E8 CC 9D 12 00                  call 0x1407d2890
006A8AC4  48 85 C0                        test rax, rax
006A8AC7  74 07                           je 0x1406a8ad0
006A8AC9  C7 40 68 DE C0 DE 35            mov dword ptr [rax + 0x68], 0x35dec0de
006A8AD0  48 83 C4 28                     add rsp, 0x28
006A8AD4  C3                              ret
006A8AD5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XpressDecodeCreate(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = CMFAllocFn(a1, 112, a3, a4);
    if (result != 0) {
        *(unsigned int *)(result + 104) = 0x35DEC0DEULL;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XpressDecodeCreate(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = CMFAllocFn(Arg1, 112, a3, a4);
    if (result != 0) {
        *(uint32_t *)(result + 0x68) = 0x35DEC0DEULL;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A8AB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A8AB4[BB_006A8AB4]
  bb_006A8AC9[BB_006A8AC9]
  bb_006A8AD0[BB_006A8AD0]
  bb_006A8AD5[BB_006A8AD5]
  bb_006A8AB4 -->|branch| bb_006A8AD0
  bb_006A8AB4 -->|fallthrough| bb_006A8AC9
  bb_006A8AC9 -->|flow| bb_006A8AD0
```
