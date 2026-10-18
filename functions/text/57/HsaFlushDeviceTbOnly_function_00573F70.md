# HsaFlushDeviceTbOnly

- RVA: `0x00573F70`–`0x00573FD9` (길이 `105` bytes)
- VA: `0x0000000140573F70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `28`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00573FC3` → [HsaIommuSendCommand](../44/HsaIommuSendCommand_function_0044E1DC.md) (function, `0x0044E1DC`)
- `0x00573FCD` → [HsaIommuWaitCommand](../44/HsaIommuWaitCommand_function_0044E1A8.md) (function, `0x0044E1A8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00573F70  40 53                           push rbx
00573F72  48 83 EC 30                     sub rsp, 0x30
00573F76  48 8B 01                        mov rax, qword ptr [rcx]
00573F79  4C 8B CA                        mov r9, rdx
00573F7C  90                              nop
00573F7D  48 8B D9                        mov rbx, rcx
00573F80  48 8B 80 20 20 00 00            mov rax, qword ptr [rax + 0x2020]
00573F87  A8 10                           test al, 0x10
00573F89  74 47                           je 0x140573fd2
00573F8B  41 0F B6 D0                     movzx edx, r8b
00573F8F  48 B8 01 F0 FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffff001
00573F99  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00573F9E  45 33 C0                        xor r8d, r8d
00573FA1  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
00573FAB  48 0B D0                        or rdx, rax
00573FAE  41 0F B7 C1                     movzx eax, r9w
00573FB2  48 C1 E2 18                     shl rdx, 0x18
00573FB6  48 0B D0                        or rdx, rax
00573FB9  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00573FBE  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00573FC3  E8 14 A2 ED FF                  call 0x14044e1dc
00573FC8  33 D2                           xor edx, edx
00573FCA  48 8B CB                        mov rcx, rbx
00573FCD  E8 D6 A1 ED FF                  call 0x14044e1a8
00573FD2  48 83 C4 30                     add rsp, 0x30
00573FD6  5B                              pop rbx
00573FD7  C3                              ret
00573FD8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HsaFlushDeviceTbOnly(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8224);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8224))) & (16)) != 0) {
        a2 = (unsigned __int8)(a3);
        v_stack_m10 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8224);
        a3 = 0;
        a2 = (a2) | (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8224));
        result = (unsigned __int16)(a2);
        a2 = (a2) << (24);
        a2 = (a2) | (result);
        v_stack_m18 = a2;
        a2 = v_stack_m18;
        result = HsaIommuSendCommand(a1, a2, a3, a2);
        a2 = 0;
        a1 = a1;
        result = HsaIommuWaitCommand(a1, a2, a3, a2);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HsaFlushDeviceTbOnly(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    result = *(uint64_t *)(*(uint64_t *)(arg1) + 0x2020);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x2020))) & (16)) != 0) {
        Arg2 = (uint8_t)(Arg3);
        v_stack_m10 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x2020);
        Arg3 = 0;
        Arg2 = (Arg2) | (*(uint64_t *)(*(uint64_t *)(arg1) + 0x2020));
        result = (uint16_t)(Arg2);
        Arg2 = (Arg2) << (24);
        Arg2 = (Arg2) | (result);
        v_stack_m18 = Arg2;
        Arg2 = v_stack_m18;
        result = HsaIommuSendCommand(Arg1, Arg2, Arg3, Arg2);
        Arg2 = 0;
        Arg1 = Arg1;
        result = HsaIommuWaitCommand(Arg1, Arg2, Arg3, Arg2);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00573F70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00573F70[BB_00573F70]
  bb_00573F8B[BB_00573F8B]
  bb_00573FD2[BB_00573FD2]
  bb_00573FD8[BB_00573FD8]
  bb_00573F70 -->|branch| bb_00573FD2
  bb_00573F70 -->|fallthrough| bb_00573F8B
  bb_00573F8B -->|flow| bb_00573FD2
```
