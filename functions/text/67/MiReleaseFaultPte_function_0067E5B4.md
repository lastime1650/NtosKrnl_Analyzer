# MiReleaseFaultPte

- RVA: `0x0067E5B4`–`0x0067E644` (길이 `144` bytes)
- VA: `0x000000014067E5B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `35`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0067E5F5` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x0067E60C` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0067E638` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) at `0x0093ED88`

### Static image references
- `0x0067E5C9` → RVA `0x00010880` (`.rdata`; read)
- `0x0067E5FA` → RVA `0x00E37408` (`.data`; read)
- `0x0067E601` → RVA `0x00E37410` (`.data`; read)
- `0x0067E611` → RVA `0x00E37414` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067E5B4  40 53                           push rbx
0067E5B6  48 83 EC 30                     sub rsp, 0x30
0067E5BA  33 C0                           xor eax, eax
0067E5BC  48 8B D9                        mov rbx, rcx
0067E5BF  48 89 44 24 24                  mov qword ptr [rsp + 0x24], rax
0067E5C4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0067E5C9  48 8B 05 B0 22 99 FF            mov rax, qword ptr [rip - 0x66dd50]
0067E5D0  48 89 01                        mov qword ptr [rcx], rax
0067E5D3  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0067E5DD  48 C1 E1 19                     shl rcx, 0x19
0067E5E1  BA 02 00 00 00                  mov edx, 2
0067E5E6  48 C1 E0 19                     shl rax, 0x19
0067E5EA  48 2B C8                        sub rcx, rax
0067E5ED  48 C1 F9 10                     sar rcx, 0x10
0067E5F1  44 8D 42 FF                     lea r8d, [rdx - 1]
0067E5F5  E8 36 01 C1 FF                  call 0x14028e730
0067E5FA  48 2B 1D 07 8E 7B 00            sub rbx, qword ptr [rip + 0x7b8e07]
0067E601  48 8D 0D 08 8E 7B 00            lea rcx, [rip + 0x7b8e08]
0067E608  48 C1 FB 03                     sar rbx, 3
0067E60C  E8 7F A0 BC FF                  call 0x140248690
0067E611  48 8D 15 FC 8D 7B 00            lea rdx, [rip + 0x7b8dfc]
0067E618  44 8B C3                        mov r8d, ebx
0067E61B  49 C1 E8 03                     shr r8, 3
0067E61F  48 8D 0D EA 8D 7B 00            lea rcx, [rip + 0x7b8dea]
0067E626  4C 03 C2                        add r8, rdx
0067E629  83 E3 07                        and ebx, 7
0067E62C  41 0F BE 10                     movsx edx, byte ptr [r8]
0067E630  0F B3 DA                        btr edx, ebx
0067E633  41 88 10                        mov byte ptr [r8], dl
0067E636  8A D0                           mov dl, al
0067E638  E8 83 9C BC FF                  call 0x1402482c0
0067E63D  48 83 C4 30                     add rsp, 0x30
0067E641  5B                              pop rbx
0067E642  C3                              ret
0067E643  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleaseFaultPte(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m14;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    result = 0;
    v_stack_m14 = 0;
    v_stack_m18 = 0;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rip - 6741328);
    a1 = (a1) << (25);
    result = (*(unsigned __int64 *)(v_rip - 6741328)) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    result = MiFlushSingleTbEntry(a1, 2, 2 - 1, a4);
    v_rbx = (a1) - (*(unsigned __int64 *)(v_rip + 8097287));
    v_rbx = (v_rbx) >> (3);
    result = ExAcquireSpinLockExclusive(v_rip + 8097288, 2, 2 - 1, a4);
    a3 = ((unsigned int)((unsigned int)(v_rbx))) >> (3);
    a3 = (a3) + (v_rip + 8097276);
    v_rbx = (unsigned int)((v_rbx) & (7));
    *(unsigned __int8 *)(a3) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a3)));
    result = MiReleaseSpinLockExclusive(v_rip + 8097258, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleaseFaultPte(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m14;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    result = 0;
    v_stack_m14 = 0;
    v_stack_m18 = 0;
    *(uint64_t *)(arg1) = *(uint64_t *)(v_rip - 0x66DD50);
    Arg1 = (Arg1) << (25);
    result = (*(uint64_t *)(v_rip - 0x66DD50)) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    result = MiFlushSingleTbEntry(Arg1, 2, 2 - 1, a4);
    local_rbx = (Arg1) - (*(uint64_t *)(v_rip + 0x7B8E07));
    local_rbx = (local_rbx) >> (3);
    result = ExAcquireSpinLockExclusive(v_rip + 8097288, 2, 2 - 1, a4);
    a3 = ((uint32_t)((uint32_t)(local_rbx))) >> (3);
    a3 = (a3) + (v_rip + 8097276);
    local_rbx = (uint32_t)((local_rbx) & (7));
    *(uint8_t *)(a3) = (uint8_t)((int8_t)(*(uint8_t *)(a3)));
    result = MiReleaseSpinLockExclusive(v_rip + 8097258, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067E5B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0067E5B4[BB_0067E5B4]
  bb_0067E643[BB_0067E643]
```
