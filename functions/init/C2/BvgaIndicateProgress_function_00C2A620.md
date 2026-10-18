# BvgaIndicateProgress

- RVA: `0x00C2A620`–`0x00C2A662` (길이 `66` bytes)
- VA: `0x0000000140C2A620`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00C2A657` → [BvgaUpdateProgressBar](../../text/59/BvgaUpdateProgressBar_function_00591930.md) (function, `0x00591930`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C2A624` → RVA `0x01008180` (`INITDATA`; read)
- `0x00C2A633` → RVA `0x01008180` (`INITDATA`; write)
- `0x00C2A63C` → RVA `0x01008184` (`INITDATA`; read)
- `0x00C2A647` → RVA `0x01008188` (`INITDATA`; read)
- `0x00C2A651` → RVA `0x01008188` (`INITDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C2A657` → [BvgaUpdateProgressBar](../../text/59/BvgaUpdateProgressBar_function_00591930.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C2A620  48 83 EC 28                     sub rsp, 0x28
00C2A624  8B 05 56 DB 3D 00               mov eax, dword ptr [rip + 0x3ddb56]
00C2A62A  33 D2                           xor edx, edx
00C2A62C  FF C0                           inc eax
00C2A62E  B9 63 00 00 00                  mov ecx, 0x63
00C2A633  89 05 47 DB 3D 00               mov dword ptr [rip + 0x3ddb47], eax
00C2A639  6B C0 64                        imul eax, eax, 0x64
00C2A63C  F7 35 42 DB 3D 00               div dword ptr [rip + 0x3ddb42]
00C2A642  3B C1                           cmp eax, ecx
00C2A644  0F 47 C1                        cmova eax, ecx
00C2A647  3B 05 3B DB 3D 00               cmp eax, dword ptr [rip + 0x3ddb3b]
00C2A64D  74 0D                           je 0x140c2a65c
00C2A64F  8B C8                           mov ecx, eax
00C2A651  89 05 31 DB 3D 00               mov dword ptr [rip + 0x3ddb31], eax
00C2A657  E8 D4 72 96 FF                  call 0x140591930
00C2A65C  48 83 C4 28                     add rsp, 0x28
00C2A660  C3                              ret
00C2A661  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BvgaIndicateProgress(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4053846))) + 1);
    *(unsigned int *)(v_rip + 4053831) = (unsigned int)(result);
    result = (unsigned int)((result) * ((unsigned int)(result)));
    if (((unsigned int)(result)) > 99) { result = 99; }
    if (((unsigned int)(result)) != (*(unsigned int *)(v_rip + 4053819))) {
        a1 = (unsigned int)(result);
        *(unsigned int *)(v_rip + 4053809) = (unsigned int)(result);
        result = BvgaUpdateProgressBar(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BvgaIndicateProgress(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3DDB56))) + 1);
    *(uint32_t *)(v_rip + 0x3DDB47) = (uint32_t)(result);
    result = (uint32_t)((result) * ((uint32_t)(result)));
    if (((uint32_t)(result)) > 99) { result = 99; }
    if (((uint32_t)(result)) != (*(uint32_t *)(v_rip + 0x3DDB3B))) {
        Arg1 = (uint32_t)(result);
        *(uint32_t *)(v_rip + 0x3DDB31) = (uint32_t)(result);
        result = BvgaUpdateProgressBar(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C2A620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C2A620[BB_00C2A620]
  bb_00C2A64F[BB_00C2A64F]
  bb_00C2A65C[BB_00C2A65C]
  bb_00C2A661[BB_00C2A661]
  bb_00C2A620 -->|branch| bb_00C2A65C
  bb_00C2A620 -->|fallthrough| bb_00C2A64F
  bb_00C2A64F -->|flow| bb_00C2A65C
```
