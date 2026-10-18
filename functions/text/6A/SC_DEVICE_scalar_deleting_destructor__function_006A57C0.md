# SC_DEVICE::`scalar deleting destructor&#x27;

- RVA: `0x006A57C0`–`0x006A57F0` (길이 `48` bytes)
- VA: `0x00000001406A57C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A57CF` → [SC_DEVICE::~SC_DEVICE](SC_DEVICE_SC_DEVICE_function_006A56F8.md) (function, `0x006A56F8`)
- `0x006A57DC` → [AlpcpFreeBuffer](../../page/90/AlpcpFreeBuffer_function_009071C0.md) (function, `0x009071C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006A57DC` → [AlpcpFreeBuffer](../../page/90/AlpcpFreeBuffer_function_009071C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A57C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006A57C5  57                              push rdi
006A57C6  48 83 EC 20                     sub rsp, 0x20
006A57CA  8B DA                           mov ebx, edx
006A57CC  48 8B F9                        mov rdi, rcx
006A57CF  E8 24 FF FF FF                  call 0x1406a56f8
006A57D4  F6 C3 01                        test bl, 1
006A57D7  74 08                           je 0x1406a57e1
006A57D9  48 8B CF                        mov rcx, rdi
006A57DC  E8 DF 19 26 00                  call 0x1409071c0
006A57E1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
006A57E6  48 8B C7                        mov rax, rdi
006A57E9  48 83 C4 20                     add rsp, 0x20
006A57ED  5F                              pop rdi
006A57EE  C3                              ret
006A57EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SC_DEVICE___scalar_deleting_destructor_(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = SC_DEVICE___SC_DEVICE(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) != 0) {
        a1 = a1;
        result = AlpcpFreeBuffer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t SC_DEVICE___scalar_deleting_destructor_(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = SC_DEVICE___SC_DEVICE(Arg1, Arg2, a3, a4);
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) != 0) {
        Arg1 = Arg1;
        result = AlpcpFreeBuffer(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A57C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A57C0[BB_006A57C0]
  bb_006A57D9[BB_006A57D9]
  bb_006A57E1[BB_006A57E1]
  bb_006A57EF[BB_006A57EF]
  bb_006A57C0 -->|branch| bb_006A57E1
  bb_006A57C0 -->|fallthrough| bb_006A57D9
  bb_006A57D9 -->|flow| bb_006A57E1
```
