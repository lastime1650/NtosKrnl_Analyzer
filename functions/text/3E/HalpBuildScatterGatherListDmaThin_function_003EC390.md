# HalpBuildScatterGatherListDmaThin

- RVA: `0x003EC390`–`0x003EC3B5` (길이 `37` bytes)
- VA: `0x00000001403EC390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095BA4`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalBuildScatterGatherListDmaThinEx](HalBuildScatterGatherListDmaThinEx_function_003EC2E0.md) at `0x003EC35F`
- [HalGetScatterGatherListDmaThinEx](../55/HalGetScatterGatherListDmaThinEx_function_00552AE0.md) at `0x00552B6D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003EC3AF` → [sub_003EC789](Unknown_function_003EC789.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003EC390  48 8B C4                        mov rax, rsp
003EC393  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
003EC397  48 89 48 08                     mov qword ptr [rax + 8], rcx
003EC39B  41 55                           push r13
003EC39D  41 56                           push r14
003EC39F  48 83 EC 68                     sub rsp, 0x68
003EC3A3  4D 8B E8                        mov r13, r8
003EC3A6  4C 8B C2                        mov r8, rdx
003EC3A9  4D 8B F1                        mov r14, r9
003EC3AC  4D 85 C9                        test r9, r9
003EC3AF  0F 84 D4 03 00 00               je 0x1403ec789
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBuildScatterGatherListDmaThin(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 v_rsp;

    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (104);
}
```

## 5. (Beta) C Style

```c
int64_t HalpBuildScatterGatherListDmaThin(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t local_rsp;

    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (104);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EC390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EC390[BB_003EC390]
```
